# Results vs. 3.13.0

- fork: brandtbucher
- ref: optimize_off_most
- machine: linux-x86_64
- commit hash: 32b9407
- commit date: 2024-11-18
- overall geometric mean: 1.064x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 300 ms: 1.13x slower                                                      |
| docutils       | 2.59 sec                                               | 3.27 sec: 1.26x slower                                                    |
| html5lib       | 64.2 ms                                                | 69.7 ms: 1.09x slower                                                     |
| sphinx         | 1.03 sec                                               | 1.22 sec: 1.18x slower                                                    |
| Geometric mean | (ref)                                                  | 1.16x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 386 ms: 1.20x faster                                                      |
| async_tree_none            | 351 ms                                                 | 342 ms: 1.02x faster                                                      |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                      |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 590 ms: 1.02x slower                                                      |
| async_tree_io              | 842 ms                                                 | 882 ms: 1.05x slower                                                      |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 573 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 985 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| float          | 79.2 ms                                                | 80.7 ms: 1.02x slower                                                     |
| nbody          | 87.0 ms                                                | 98.9 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.2 ms: 1.04x faster                                                     |
| regex_effbot   | 3.73 ms                                                | 3.80 ms: 1.02x slower                                                     |
| regex_dna      | 218 ms                                                 | 225 ms: 1.03x slower                                                      |
| regex_compile  | 132 ms                                                 | 156 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| xml_etree_generate   | 86.7 ms                                                | 83.6 ms: 1.04x faster                                                     |
| json_loads           | 27.2 us                                                | 26.4 us: 1.03x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 2.09 sec: 1.02x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.00x slower                                                      |
| unpickle_pure_python | 216 us                                                 | 228 us: 1.06x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                     |
| pickle_pure_python   | 310 us                                                 | 342 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.12 ms: 1.02x slower                                                     |
| python_startup         | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 35.4 ms: 1.01x slower                                                     |
| mako            | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                     |
| genshi_text     | 23.5 ms                                                | 27.2 ms: 1.16x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 67.6 ms: 1.33x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.12x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 32.3 us: 1.21x faster                                                     |
| deepcopy                   | 358 us                                                 | 298 us: 1.20x faster                                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 386 ms: 1.20x faster                                                      |
| telco                      | 8.54 ms                                                | 7.64 ms: 1.12x faster                                                     |
| deepcopy_reduce            | 3.20 us                                                | 2.92 us: 1.10x faster                                                     |
| json                       | 5.36 ms                                                | 4.90 ms: 1.09x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.4 ms: 1.07x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| scimark_fft                | 364 ms                                                 | 349 ms: 1.04x faster                                                      |
| regex_v8                   | 26.2 ms                                                | 25.2 ms: 1.04x faster                                                     |
| xml_etree_generate         | 86.7 ms                                                | 83.6 ms: 1.04x faster                                                     |
| json_loads                 | 27.2 us                                                | 26.4 us: 1.03x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 73.3 ms: 1.03x faster                                                     |
| async_tree_none            | 351 ms                                                 | 342 ms: 1.02x faster                                                      |
| tomli_loads                | 2.14 sec                                               | 2.09 sec: 1.02x faster                                                    |
| thrift                     | 809 us                                                 | 792 us: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.00 ms: 1.01x faster                                                     |
| gc_traversal               | 4.37 ms                                                | 4.36 ms: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| coverage                   | 84.0 ms                                                | 84.4 ms: 1.00x slower                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.00x slower                                                      |
| connected_components       | 444 ms                                                 | 447 ms: 1.01x slower                                                      |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                      |
| django_template            | 35.2 ms                                                | 35.4 ms: 1.01x slower                                                     |
| bpe_tokeniser              | 4.75 sec                                               | 4.79 sec: 1.01x slower                                                    |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                     |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                     |
| logging_format             | 6.40 us                                                | 6.47 us: 1.01x slower                                                     |
| shortest_path              | 481 ms                                                 | 487 ms: 1.01x slower                                                      |
| regex_effbot               | 3.73 ms                                                | 3.80 ms: 1.02x slower                                                     |
| float                      | 79.2 ms                                                | 80.7 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 590 ms: 1.02x slower                                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.12 ms: 1.02x slower                                                     |
| logging_simple             | 5.72 us                                                | 5.85 us: 1.02x slower                                                     |
| meteor_contest             | 109 ms                                                 | 112 ms: 1.03x slower                                                      |
| regex_dna                  | 218 ms                                                 | 225 ms: 1.03x slower                                                      |
| mdp                        | 2.72 sec                                               | 2.80 sec: 1.03x slower                                                    |
| python_startup             | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                     |
| async_tree_io              | 842 ms                                                 | 882 ms: 1.05x slower                                                      |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 573 ms: 1.05x slower                                                      |
| go                         | 144 ms                                                 | 151 ms: 1.05x slower                                                      |
| richards_super             | 54.9 ms                                                | 57.7 ms: 1.05x slower                                                     |
| scimark_lu                 | 113 ms                                                 | 119 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 165 us                                                 | 174 us: 1.06x slower                                                      |
| unpickle_pure_python       | 216 us                                                 | 228 us: 1.06x slower                                                      |
| sqlalchemy_imperative      | 17.1 ms                                                | 18.2 ms: 1.07x slower                                                     |
| pycparser                  | 1.20 sec                                               | 1.28 sec: 1.07x slower                                                    |
| pyflate                    | 471 ms                                                 | 505 ms: 1.07x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                     |
| fannkuch                   | 404 ms                                                 | 437 ms: 1.08x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 72.9 ms: 1.08x slower                                                     |
| html5lib                   | 64.2 ms                                                | 69.7 ms: 1.09x slower                                                     |
| dulwich_log                | 64.3 ms                                                | 70.8 ms: 1.10x slower                                                     |
| pickle_pure_python         | 310 us                                                 | 342 us: 1.10x slower                                                      |
| spectral_norm              | 115 ms                                                 | 127 ms: 1.10x slower                                                      |
| logging_silent             | 102 ns                                                 | 112 ns: 1.11x slower                                                      |
| create_gc_cycles           | 2.41 ms                                                | 2.68 ms: 1.11x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 915 us: 1.11x slower                                                      |
| scimark_sor                | 124 ms                                                 | 138 ms: 1.12x slower                                                      |
| 2to3                       | 267 ms                                                 | 300 ms: 1.13x slower                                                      |
| sqlglot_normalize          | 108 ms                                                 | 122 ms: 1.13x slower                                                      |
| nbody                      | 87.0 ms                                                | 98.9 ms: 1.14x slower                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 152 ms: 1.14x slower                                                      |
| raytrace                   | 267 ms                                                 | 304 ms: 1.14x slower                                                      |
| sympy_expand               | 463 ms                                                 | 530 ms: 1.14x slower                                                      |
| chaos                      | 58.1 ms                                                | 66.7 ms: 1.15x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 985 ms: 1.15x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.47 ms: 1.15x slower                                                     |
| genshi_text                | 23.5 ms                                                | 27.2 ms: 1.16x slower                                                     |
| deltablue                  | 3.23 ms                                                | 3.73 ms: 1.16x slower                                                     |
| sympy_str                  | 275 ms                                                 | 323 ms: 1.17x slower                                                      |
| sphinx                     | 1.03 sec                                               | 1.22 sec: 1.18x slower                                                    |
| comprehensions             | 16.5 us                                                | 19.4 us: 1.18x slower                                                     |
| regex_compile              | 132 ms                                                 | 156 ms: 1.18x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.89 ms: 1.19x slower                                                     |
| nqueens                    | 78.4 ms                                                | 94.2 ms: 1.20x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 64.7 ms: 1.20x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 188 ms: 1.25x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 910 ms: 1.25x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 25.1 ms: 1.26x slower                                                     |
| docutils                   | 2.59 sec                                               | 3.27 sec: 1.26x slower                                                    |
| pylint                     | 313 ms                                                 | 395 ms: 1.26x slower                                                      |
| pprint_pformat             | 1.49 sec                                               | 1.89 sec: 1.27x slower                                                    |
| genshi_xml                 | 50.9 ms                                                | 67.6 ms: 1.33x slower                                                     |
| hexiom                     | 6.16 ms                                                | 8.25 ms: 1.34x slower                                                     |
| generators                 | 29.0 ms                                                | 41.0 ms: 1.42x slower                                                     |
| k_core                     | 2.35 sec                                               | 3.63 sec: 1.54x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 86.6 ms: 3.61x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                              |

Benchmark hidden because not significant (4): async_tree_memoization, xml_etree_process, richards, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241118-3.14.0a1+-32b9407-JIT/bm-20241118-linux-x86_64-brandtbucher-optimize_off_most-3.14.0a1+-32b9407.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.064x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x