# Results vs. 3.13.0

- fork: brandtbucher
- ref: jb0_backoff
- machine: linux-x86_64
- commit hash: 50d9e07
- commit date: 2024-10-24
- overall geometric mean: 1.046x slower
- HPT reliability: 97.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 286 ms: 1.07x slower                                                |
| docutils       | 2.59 sec                                               | 3.40 sec: 1.31x slower                                              |
| html5lib       | 64.2 ms                                                | 68.6 ms: 1.07x slower                                               |
| sphinx         | 1.03 sec                                               | 1.35 sec: 1.30x slower                                              |
| tornado_http   | 92.4 ms                                                | 112 ms: 1.21x slower                                                |
| Geometric mean | (ref)                                                  | 1.19x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 405 ms: 1.14x faster                                                |
| asyncio_websockets         | 552 ms                                                 | 557 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 599 ms: 1.04x slower                                                |
| async_tree_none_tg         | 321 ms                                                 | 338 ms: 1.05x slower                                                |
| async_generators           | 436 ms                                                 | 467 ms: 1.07x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 589 ms: 1.08x slower                                                |
| async_tree_io              | 842 ms                                                 | 941 ms: 1.12x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 959 ms: 1.12x slower                                                |
| coroutines                 | 22.7 ms                                                | 26.4 ms: 1.16x slower                                               |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                        |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 81.7 ms: 1.06x faster                                               |
| float          | 79.2 ms                                                | 75.0 ms: 1.06x faster                                               |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.8 ms: 1.02x faster                                               |
| regex_dna      | 218 ms                                                 | 215 ms: 1.01x faster                                                |
| regex_effbot   | 3.73 ms                                                | 3.71 ms: 1.00x faster                                               |
| regex_compile  | 132 ms                                                 | 146 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.10x faster                                              |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                |
| pickle_pure_python   | 310 us                                                 | 294 us: 1.06x faster                                                |
| xml_etree_generate   | 86.7 ms                                                | 83.3 ms: 1.04x faster                                               |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                               |
| xml_etree_process    | 60.6 ms                                                | 60.1 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                                |
| unpickle_pure_python | 216 us                                                 | 226 us: 1.05x slower                                                |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.9 ms: 1.05x faster                                               |
| python_startup_no_site | 6.96 ms                                                | 7.11 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.09x faster                                               |
| genshi_text     | 23.5 ms                                                | 25.7 ms: 1.09x slower                                               |
| django_template | 35.2 ms                                                | 40.5 ms: 1.15x slower                                               |
| genshi_xml      | 50.9 ms                                                | 62.6 ms: 1.23x slower                                               |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.7 us: 1.32x faster                                               |
| deepcopy                   | 358 us                                                 | 277 us: 1.29x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 405 ms: 1.14x faster                                                |
| scimark_fft                | 364 ms                                                 | 321 ms: 1.13x faster                                                |
| telco                      | 8.54 ms                                                | 7.61 ms: 1.12x faster                                               |
| go                         | 144 ms                                                 | 129 ms: 1.11x faster                                                |
| crypto_pyaes               | 75.3 ms                                                | 67.9 ms: 1.11x faster                                               |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.10x faster                                              |
| deepcopy_reduce            | 3.20 us                                                | 2.91 us: 1.10x faster                                               |
| scimark_monte_carlo        | 67.4 ms                                                | 61.7 ms: 1.09x faster                                               |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.09x faster                                               |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.66 ms: 1.08x faster                                               |
| json                       | 5.36 ms                                                | 4.99 ms: 1.07x faster                                               |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                |
| bpe_tokeniser              | 4.75 sec                                               | 4.46 sec: 1.07x faster                                              |
| nbody                      | 87.0 ms                                                | 81.7 ms: 1.06x faster                                               |
| pickle_pure_python         | 310 us                                                 | 294 us: 1.06x faster                                                |
| pathlib                    | 17.5 ms                                                | 16.6 ms: 1.06x faster                                               |
| float                      | 79.2 ms                                                | 75.0 ms: 1.06x faster                                               |
| pyflate                    | 471 ms                                                 | 446 ms: 1.05x faster                                                |
| fannkuch                   | 404 ms                                                 | 384 ms: 1.05x faster                                                |
| python_startup             | 12.5 ms                                                | 11.9 ms: 1.05x faster                                               |
| xml_etree_generate         | 86.7 ms                                                | 83.3 ms: 1.04x faster                                               |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                               |
| regex_v8                   | 26.2 ms                                                | 25.8 ms: 1.02x faster                                               |
| regex_dna                  | 218 ms                                                 | 215 ms: 1.01x faster                                                |
| scimark_sor                | 124 ms                                                 | 122 ms: 1.01x faster                                                |
| mdp                        | 2.72 sec                                               | 2.69 sec: 1.01x faster                                              |
| xml_etree_process          | 60.6 ms                                                | 60.1 ms: 1.01x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                                |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                |
| regex_effbot               | 3.73 ms                                                | 3.71 ms: 1.00x faster                                               |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| asyncio_websockets         | 552 ms                                                 | 557 ms: 1.01x slower                                                |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.01x slower                                                |
| thrift                     | 809 us                                                 | 825 us: 1.02x slower                                                |
| python_startup_no_site     | 6.96 ms                                                | 7.11 ms: 1.02x slower                                               |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                |
| coverage                   | 84.0 ms                                                | 86.4 ms: 1.03x slower                                               |
| chaos                      | 58.1 ms                                                | 59.8 ms: 1.03x slower                                               |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 599 ms: 1.04x slower                                                |
| logging_silent             | 102 ns                                                 | 106 ns: 1.04x slower                                                |
| unpickle_pure_python       | 216 us                                                 | 226 us: 1.05x slower                                                |
| async_tree_none_tg         | 321 ms                                                 | 338 ms: 1.05x slower                                                |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                               |
| pycparser                  | 1.20 sec                                               | 1.27 sec: 1.06x slower                                              |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                               |
| html5lib                   | 64.2 ms                                                | 68.6 ms: 1.07x slower                                               |
| async_generators           | 436 ms                                                 | 467 ms: 1.07x slower                                                |
| 2to3                       | 267 ms                                                 | 286 ms: 1.07x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 589 ms: 1.08x slower                                                |
| gc_traversal               | 4.37 ms                                                | 4.74 ms: 1.08x slower                                               |
| dulwich_log                | 64.3 ms                                                | 70.0 ms: 1.09x slower                                               |
| genshi_text                | 23.5 ms                                                | 25.7 ms: 1.09x slower                                               |
| create_gc_cycles           | 2.41 ms                                                | 2.66 ms: 1.11x slower                                               |
| regex_compile              | 132 ms                                                 | 146 ms: 1.11x slower                                                |
| raytrace                   | 267 ms                                                 | 296 ms: 1.11x slower                                                |
| sqlglot_normalize          | 108 ms                                                 | 120 ms: 1.11x slower                                                |
| async_tree_io              | 842 ms                                                 | 941 ms: 1.12x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 959 ms: 1.12x slower                                                |
| sqlglot_parse              | 1.27 ms                                                | 1.43 ms: 1.13x slower                                               |
| nqueens                    | 78.4 ms                                                | 89.3 ms: 1.14x slower                                               |
| sympy_expand               | 463 ms                                                 | 533 ms: 1.15x slower                                                |
| django_template            | 35.2 ms                                                | 40.5 ms: 1.15x slower                                               |
| coroutines                 | 22.7 ms                                                | 26.4 ms: 1.16x slower                                               |
| sqlglot_transpile          | 1.58 ms                                                | 1.85 ms: 1.17x slower                                               |
| bench_thread_pool          | 822 us                                                 | 969 us: 1.18x slower                                                |
| logging_format             | 6.40 us                                                | 7.57 us: 1.18x slower                                               |
| hexiom                     | 6.16 ms                                                | 7.44 ms: 1.21x slower                                               |
| tornado_http               | 92.4 ms                                                | 112 ms: 1.21x slower                                                |
| sympy_str                  | 275 ms                                                 | 334 ms: 1.22x slower                                                |
| logging_simple             | 5.72 us                                                | 7.01 us: 1.23x slower                                               |
| genshi_xml                 | 50.9 ms                                                | 62.6 ms: 1.23x slower                                               |
| sqlglot_optimize           | 53.7 ms                                                | 66.7 ms: 1.24x slower                                               |
| deltablue                  | 3.23 ms                                                | 4.04 ms: 1.25x slower                                               |
| generators                 | 29.0 ms                                                | 36.6 ms: 1.26x slower                                               |
| sphinx                     | 1.03 sec                                               | 1.35 sec: 1.30x slower                                              |
| docutils                   | 2.59 sec                                               | 3.40 sec: 1.31x slower                                              |
| sqlalchemy_declarative     | 133 ms                                                 | 175 ms: 1.31x slower                                                |
| sqlalchemy_imperative      | 17.1 ms                                                | 22.5 ms: 1.32x slower                                               |
| sympy_sum                  | 150 ms                                                 | 206 ms: 1.37x slower                                                |
| sympy_integrate            | 19.9 ms                                                | 27.3 ms: 1.37x slower                                               |
| pylint                     | 313 ms                                                 | 466 ms: 1.49x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 89.0 ms: 3.71x slower                                               |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                        |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_none, pprint_pformat, richards_super, pprint_safe_repr, richards, scimark_lu
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.046x slower
# HPT report

- Reliability score: 97.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x