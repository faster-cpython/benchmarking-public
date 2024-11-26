# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 7e6deef
- commit date: 2024-10-29
- overall geometric mean: 1.507x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 2.01x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 530 ms: 1.99x slower                                                      |
| docutils       | 2.59 sec                                               | 5.45 sec: 2.10x slower                                                    |
| html5lib       | 64.2 ms                                                | 130 ms: 2.02x slower                                                      |
| sphinx         | 1.03 sec                                               | 2.16 sec: 2.09x slower                                                    |
| tornado_http   | 92.4 ms                                                | 187 ms: 2.02x slower                                                      |
| Geometric mean | (ref)                                                  | 2.04x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 781 ms: 1.68x slower                                                      |
| async_tree_none            | 351 ms                                                 | 687 ms: 1.96x slower                                                      |
| async_tree_memoization     | 442 ms                                                 | 878 ms: 1.99x slower                                                      |
| asyncio_websockets         | 552 ms                                                 | 1.11 sec: 2.01x slower                                                    |
| async_generators           | 436 ms                                                 | 882 ms: 2.02x slower                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 1.17 sec: 2.03x slower                                                    |
| async_tree_none_tg         | 321 ms                                                 | 659 ms: 2.06x slower                                                      |
| async_tree_io              | 842 ms                                                 | 1.75 sec: 2.08x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 1.16 sec: 2.13x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 1.85 sec: 2.16x slower                                                    |
| coroutines                 | 22.7 ms                                                | 50.5 ms: 2.22x slower                                                     |
| Geometric mean             | (ref)                                                  | 2.03x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 378 ms: 2.03x slower                                                      |
| float          | 79.2 ms                                                | 161 ms: 2.04x slower                                                      |
| nbody          | 87.0 ms                                                | 195 ms: 2.24x slower                                                      |
| Geometric mean | (ref)                                                  | 2.10x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 49.1 ms: 1.87x slower                                                     |
| regex_compile  | 132 ms                                                 | 264 ms: 1.99x slower                                                      |
| regex_effbot   | 3.73 ms                                                | 7.47 ms: 2.00x slower                                                     |
| regex_dna      | 218 ms                                                 | 439 ms: 2.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.97x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 53.4 us: 1.96x slower                                                     |
| tomli_loads          | 2.14 sec                                               | 4.25 sec: 1.98x slower                                                    |
| xml_etree_parse      | 156 ms                                                 | 314 ms: 2.02x slower                                                      |
| xml_etree_process    | 60.6 ms                                                | 123 ms: 2.02x slower                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 206 ms: 2.03x slower                                                      |
| xml_etree_generate   | 86.7 ms                                                | 177 ms: 2.04x slower                                                      |
| pickle_pure_python   | 310 us                                                 | 635 us: 2.05x slower                                                      |
| unpickle_pure_python | 216 us                                                 | 445 us: 2.06x slower                                                      |
| json_dumps           | 10.6 ms                                                | 23.2 ms: 2.20x slower                                                     |
| Geometric mean       | (ref)                                                  | 2.04x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 15.7 ms: 2.26x slower                                                     |
| python_startup         | 12.5 ms                                                | 31.0 ms: 2.48x slower                                                     |
| Geometric mean         | (ref)                                                  | 2.37x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 45.3 ms: 1.92x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 104 ms: 2.05x slower                                                      |
| django_template | 35.2 ms                                                | 72.1 ms: 2.05x slower                                                     |
| mako            | 11.1 ms                                                | 23.3 ms: 2.10x slower                                                     |
| Geometric mean  | (ref)                                                  | 2.03x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-7e6deef |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 533 us: 1.49x slower                                                      |
| deepcopy_memo              | 39.1 us                                                | 58.7 us: 1.50x slower                                                     |
| async_tree_memoization_tg  | 464 ms                                                 | 781 ms: 1.68x slower                                                      |
| go                         | 144 ms                                                 | 242 ms: 1.68x slower                                                      |
| deepcopy_reduce            | 3.20 us                                                | 5.62 us: 1.76x slower                                                     |
| json                       | 5.36 ms                                                | 9.80 ms: 1.83x slower                                                     |
| mdp                        | 2.72 sec                                               | 5.02 sec: 1.85x slower                                                    |
| pathlib                    | 17.5 ms                                                | 32.6 ms: 1.86x slower                                                     |
| regex_v8                   | 26.2 ms                                                | 49.1 ms: 1.87x slower                                                     |
| telco                      | 8.54 ms                                                | 16.2 ms: 1.90x slower                                                     |
| logging_silent             | 102 ns                                                 | 193 ns: 1.90x slower                                                      |
| richards                   | 48.7 ms                                                | 92.4 ms: 1.90x slower                                                     |
| richards_super             | 54.9 ms                                                | 105 ms: 1.92x slower                                                      |
| genshi_text                | 23.5 ms                                                | 45.3 ms: 1.92x slower                                                     |
| async_tree_none            | 351 ms                                                 | 687 ms: 1.96x slower                                                      |
| json_loads                 | 27.2 us                                                | 53.4 us: 1.96x slower                                                     |
| thrift                     | 809 us                                                 | 1.59 ms: 1.97x slower                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 9.96 ms: 1.97x slower                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 264 ms: 1.98x slower                                                      |
| meteor_contest             | 109 ms                                                 | 216 ms: 1.98x slower                                                      |
| tomli_loads                | 2.14 sec                                               | 4.25 sec: 1.98x slower                                                    |
| async_tree_memoization     | 442 ms                                                 | 878 ms: 1.99x slower                                                      |
| crypto_pyaes               | 75.3 ms                                                | 150 ms: 1.99x slower                                                      |
| 2to3                       | 267 ms                                                 | 530 ms: 1.99x slower                                                      |
| spectral_norm              | 115 ms                                                 | 230 ms: 1.99x slower                                                      |
| regex_compile              | 132 ms                                                 | 264 ms: 1.99x slower                                                      |
| coverage                   | 84.0 ms                                                | 167 ms: 1.99x slower                                                      |
| regex_effbot               | 3.73 ms                                                | 7.47 ms: 2.00x slower                                                     |
| deltablue                  | 3.23 ms                                                | 6.46 ms: 2.00x slower                                                     |
| bpe_tokeniser              | 4.75 sec                                               | 9.50 sec: 2.00x slower                                                    |
| asyncio_websockets         | 552 ms                                                 | 1.11 sec: 2.01x slower                                                    |
| pycparser                  | 1.20 sec                                               | 2.41 sec: 2.01x slower                                                    |
| gc_traversal               | 4.37 ms                                                | 8.77 ms: 2.01x slower                                                     |
| typing_runtime_protocols   | 165 us                                                 | 331 us: 2.01x slower                                                      |
| regex_dna                  | 218 ms                                                 | 439 ms: 2.01x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 303 ms: 2.01x slower                                                      |
| sympy_str                  | 275 ms                                                 | 553 ms: 2.01x slower                                                      |
| dulwich_log                | 64.3 ms                                                | 130 ms: 2.02x slower                                                      |
| xml_etree_parse            | 156 ms                                                 | 314 ms: 2.02x slower                                                      |
| xml_etree_process          | 60.6 ms                                                | 123 ms: 2.02x slower                                                      |
| tornado_http               | 92.4 ms                                                | 187 ms: 2.02x slower                                                      |
| html5lib                   | 64.2 ms                                                | 130 ms: 2.02x slower                                                      |
| async_generators           | 436 ms                                                 | 882 ms: 2.02x slower                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 1.17 sec: 2.03x slower                                                    |
| raytrace                   | 267 ms                                                 | 542 ms: 2.03x slower                                                      |
| pidigits                   | 186 ms                                                 | 378 ms: 2.03x slower                                                      |
| generators                 | 29.0 ms                                                | 58.8 ms: 2.03x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 40.5 ms: 2.03x slower                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 206 ms: 2.03x slower                                                      |
| sympy_expand               | 463 ms                                                 | 943 ms: 2.03x slower                                                      |
| float                      | 79.2 ms                                                | 161 ms: 2.04x slower                                                      |
| xml_etree_generate         | 86.7 ms                                                | 177 ms: 2.04x slower                                                      |
| sqlglot_normalize          | 108 ms                                                 | 219 ms: 2.04x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 635 us: 2.05x slower                                                      |
| genshi_xml                 | 50.9 ms                                                | 104 ms: 2.05x slower                                                      |
| scimark_fft                | 364 ms                                                 | 746 ms: 2.05x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 138 ms: 2.05x slower                                                      |
| django_template            | 35.2 ms                                                | 72.1 ms: 2.05x slower                                                     |
| async_tree_none_tg         | 321 ms                                                 | 659 ms: 2.06x slower                                                      |
| pprint_pformat             | 1.49 sec                                               | 3.07 sec: 2.06x slower                                                    |
| sqlglot_parse              | 1.27 ms                                                | 2.62 ms: 2.06x slower                                                     |
| scimark_lu                 | 113 ms                                                 | 232 ms: 2.06x slower                                                      |
| logging_format             | 6.40 us                                                | 13.2 us: 2.06x slower                                                     |
| pprint_safe_repr           | 728 ms                                                 | 1.50 sec: 2.06x slower                                                    |
| unpickle_pure_python       | 216 us                                                 | 445 us: 2.06x slower                                                      |
| sqlalchemy_imperative      | 17.1 ms                                                | 35.3 ms: 2.07x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 3.28 ms: 2.07x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 112 ms: 2.08x slower                                                      |
| async_tree_io              | 842 ms                                                 | 1.75 sec: 2.08x slower                                                    |
| sphinx                     | 1.03 sec                                               | 2.16 sec: 2.09x slower                                                    |
| hexiom                     | 6.16 ms                                                | 12.9 ms: 2.09x slower                                                     |
| pylint                     | 313 ms                                                 | 653 ms: 2.09x slower                                                      |
| logging_simple             | 5.72 us                                                | 11.9 us: 2.09x slower                                                     |
| pyflate                    | 471 ms                                                 | 987 ms: 2.10x slower                                                      |
| mako                       | 11.1 ms                                                | 23.3 ms: 2.10x slower                                                     |
| docutils                   | 2.59 sec                                               | 5.45 sec: 2.10x slower                                                    |
| comprehensions             | 16.5 us                                                | 34.9 us: 2.12x slower                                                     |
| fannkuch                   | 404 ms                                                 | 859 ms: 2.12x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 1.16 sec: 2.13x slower                                                    |
| connected_components       | 444 ms                                                 | 949 ms: 2.14x slower                                                      |
| shortest_path              | 481 ms                                                 | 1.03 sec: 2.14x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 1.85 sec: 2.16x slower                                                    |
| chaos                      | 58.1 ms                                                | 126 ms: 2.17x slower                                                      |
| create_gc_cycles           | 2.41 ms                                                | 5.24 ms: 2.18x slower                                                     |
| scimark_sor                | 124 ms                                                 | 270 ms: 2.18x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 23.2 ms: 2.20x slower                                                     |
| nqueens                    | 78.4 ms                                                | 173 ms: 2.21x slower                                                      |
| coroutines                 | 22.7 ms                                                | 50.5 ms: 2.22x slower                                                     |
| nbody                      | 87.0 ms                                                | 195 ms: 2.24x slower                                                      |
| python_startup_no_site     | 6.96 ms                                                | 15.7 ms: 2.26x slower                                                     |
| python_startup             | 12.5 ms                                                | 31.0 ms: 2.48x slower                                                     |
| k_core                     | 2.35 sec                                               | 7.32 sec: 3.11x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 128 ms: 5.33x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 30.3 ms: 36.86x slower                                                    |
| Geometric mean             | (ref)                                                  | 2.11x slower                                                              |
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2

- Geometric mean (including insignificant results): 1.507x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 2.02x
- 95% likely to have a slowdown of 2.02x
- 99% likely to have a slowdown of 2.01x

# Memory
- memory change: 1.01x