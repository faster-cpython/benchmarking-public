# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.085x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 301 ms: 1.13x slower                                                      |
| docutils       | 2.59 sec                                               | 3.01 sec: 1.16x slower                                                    |
| html5lib       | 64.2 ms                                                | 68.6 ms: 1.07x slower                                                     |
| sphinx         | 1.03 sec                                               | 1.21 sec: 1.17x slower                                                    |
| tornado_http   | 92.4 ms                                                | 96.7 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 589 ms: 1.02x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                     |
| async_tree_none_tg         | 321 ms                                                 | 331 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 565 ms: 1.04x slower                                                      |
| async_tree_io              | 842 ms                                                 | 880 ms: 1.05x slower                                                      |
| async_generators           | 436 ms                                                 | 464 ms: 1.07x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 985 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_none, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                      |
| float          | 79.2 ms                                                | 83.5 ms: 1.05x slower                                                     |
| nbody          | 87.0 ms                                                | 102 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                  | 1.08x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 218 ms                                                 | 213 ms: 1.03x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                     |
| regex_v8       | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                     |
| regex_compile  | 132 ms                                                 | 154 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 152 ms: 1.02x faster                                                      |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 2.18 sec: 1.02x slower                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.04x slower                                                      |
| xml_etree_generate   | 86.7 ms                                                | 90.4 ms: 1.04x slower                                                     |
| xml_etree_process    | 60.6 ms                                                | 63.7 ms: 1.05x slower                                                     |
| json_dumps           | 10.6 ms                                                | 11.7 ms: 1.11x slower                                                     |
| pickle_pure_python   | 310 us                                                 | 349 us: 1.13x slower                                                      |
| unpickle_pure_python | 216 us                                                 | 248 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.8 ms: 1.06x faster                                                     |
| python_startup_no_site | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 12.1 ms: 1.09x slower                                                     |
| django_template | 35.2 ms                                                | 39.2 ms: 1.11x slower                                                     |
| genshi_text     | 23.5 ms                                                | 27.6 ms: 1.17x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 64.5 ms: 1.27x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.16x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                      |
| deepcopy                   | 358 us                                                 | 309 us: 1.16x faster                                                      |
| deepcopy_memo              | 39.1 us                                                | 35.3 us: 1.11x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.4 ms: 1.07x faster                                                     |
| python_startup             | 12.5 ms                                                | 11.8 ms: 1.06x faster                                                     |
| deepcopy_reduce            | 3.20 us                                                | 3.07 us: 1.04x faster                                                     |
| json                       | 5.36 ms                                                | 5.15 ms: 1.04x faster                                                     |
| regex_dna                  | 218 ms                                                 | 213 ms: 1.03x faster                                                      |
| mdp                        | 2.72 sec                                               | 2.66 sec: 1.02x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 152 ms: 1.02x faster                                                      |
| regex_effbot               | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                     |
| logging_format             | 6.40 us                                                | 6.27 us: 1.02x faster                                                     |
| telco                      | 8.54 ms                                                | 8.42 ms: 1.01x faster                                                     |
| regex_v8                   | 26.2 ms                                                | 25.9 ms: 1.01x faster                                                     |
| thrift                     | 809 us                                                 | 801 us: 1.01x faster                                                      |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                                     |
| coverage                   | 84.0 ms                                                | 84.6 ms: 1.01x slower                                                     |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                     |
| tomli_loads                | 2.14 sec                                               | 2.18 sec: 1.02x slower                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 589 ms: 1.02x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                     |
| async_tree_none_tg         | 321 ms                                                 | 331 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 565 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.23 ms: 1.04x slower                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.04x slower                                                      |
| xml_etree_generate         | 86.7 ms                                                | 90.4 ms: 1.04x slower                                                     |
| async_tree_io              | 842 ms                                                 | 880 ms: 1.05x slower                                                      |
| tornado_http               | 92.4 ms                                                | 96.7 ms: 1.05x slower                                                     |
| scimark_fft                | 364 ms                                                 | 382 ms: 1.05x slower                                                      |
| xml_etree_process          | 60.6 ms                                                | 63.7 ms: 1.05x slower                                                     |
| float                      | 79.2 ms                                                | 83.5 ms: 1.05x slower                                                     |
| sqlalchemy_imperative      | 17.1 ms                                                | 18.1 ms: 1.06x slower                                                     |
| async_generators           | 436 ms                                                 | 464 ms: 1.07x slower                                                      |
| html5lib                   | 64.2 ms                                                | 68.6 ms: 1.07x slower                                                     |
| dulwich_log                | 64.3 ms                                                | 68.9 ms: 1.07x slower                                                     |
| pycparser                  | 1.20 sec                                               | 1.29 sec: 1.07x slower                                                    |
| gc_traversal               | 4.37 ms                                                | 4.70 ms: 1.07x slower                                                     |
| pylint                     | 313 ms                                                 | 337 ms: 1.08x slower                                                      |
| scimark_lu                 | 113 ms                                                 | 123 ms: 1.09x slower                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 5.17 sec: 1.09x slower                                                    |
| mako                       | 11.1 ms                                                | 12.1 ms: 1.09x slower                                                     |
| json_dumps                 | 10.6 ms                                                | 11.7 ms: 1.11x slower                                                     |
| typing_runtime_protocols   | 165 us                                                 | 183 us: 1.11x slower                                                      |
| django_template            | 35.2 ms                                                | 39.2 ms: 1.11x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.69 ms: 1.12x slower                                                     |
| richards_super             | 54.9 ms                                                | 61.5 ms: 1.12x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 921 us: 1.12x slower                                                      |
| crypto_pyaes               | 75.3 ms                                                | 84.6 ms: 1.12x slower                                                     |
| meteor_contest             | 109 ms                                                 | 122 ms: 1.12x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 349 us: 1.13x slower                                                      |
| pyflate                    | 471 ms                                                 | 531 ms: 1.13x slower                                                      |
| 2to3                       | 267 ms                                                 | 301 ms: 1.13x slower                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 151 ms: 1.13x slower                                                      |
| sympy_expand               | 463 ms                                                 | 525 ms: 1.13x slower                                                      |
| go                         | 144 ms                                                 | 165 ms: 1.15x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 985 ms: 1.15x slower                                                      |
| unpickle_pure_python       | 216 us                                                 | 248 us: 1.15x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.47 ms: 1.15x slower                                                     |
| docutils                   | 2.59 sec                                               | 3.01 sec: 1.16x slower                                                    |
| sqlglot_normalize          | 108 ms                                                 | 125 ms: 1.16x slower                                                      |
| regex_compile              | 132 ms                                                 | 154 ms: 1.16x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.84 ms: 1.16x slower                                                     |
| sympy_str                  | 275 ms                                                 | 321 ms: 1.17x slower                                                      |
| spectral_norm              | 115 ms                                                 | 135 ms: 1.17x slower                                                      |
| genshi_text                | 23.5 ms                                                | 27.6 ms: 1.17x slower                                                     |
| sphinx                     | 1.03 sec                                               | 1.21 sec: 1.17x slower                                                    |
| nbody                      | 87.0 ms                                                | 102 ms: 1.18x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 870 ms: 1.20x slower                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 80.7 ms: 1.20x slower                                                     |
| logging_silent             | 102 ns                                                 | 122 ns: 1.20x slower                                                      |
| fannkuch                   | 404 ms                                                 | 486 ms: 1.20x slower                                                      |
| pprint_pformat             | 1.49 sec                                               | 1.81 sec: 1.21x slower                                                    |
| richards                   | 48.7 ms                                                | 59.1 ms: 1.21x slower                                                     |
| deltablue                  | 3.23 ms                                                | 3.93 ms: 1.22x slower                                                     |
| scimark_sor                | 124 ms                                                 | 151 ms: 1.22x slower                                                      |
| sqlglot_optimize           | 53.7 ms                                                | 65.7 ms: 1.22x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 184 ms: 1.22x slower                                                      |
| raytrace                   | 267 ms                                                 | 327 ms: 1.23x slower                                                      |
| chaos                      | 58.1 ms                                                | 72.9 ms: 1.26x slower                                                     |
| genshi_xml                 | 50.9 ms                                                | 64.5 ms: 1.27x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 25.2 ms: 1.27x slower                                                     |
| comprehensions             | 16.5 us                                                | 22.0 us: 1.33x slower                                                     |
| nqueens                    | 78.4 ms                                                | 107 ms: 1.36x slower                                                      |
| hexiom                     | 6.16 ms                                                | 8.79 ms: 1.43x slower                                                     |
| generators                 | 29.0 ms                                                | 41.6 ms: 1.43x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 84.6 ms: 3.53x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.11x slower                                                              |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none, asyncio_websockets, logging_simple
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.085x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.07x