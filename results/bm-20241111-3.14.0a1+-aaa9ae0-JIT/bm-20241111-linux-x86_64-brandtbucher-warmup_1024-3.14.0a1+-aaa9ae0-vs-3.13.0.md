# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_1024
- machine: linux-x86_64
- commit hash: aaa9ae0
- commit date: 2024-11-11
- overall geometric mean: 1.004x faster
- HPT reliability: 72.28%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 269 ms: 1.01x slower                                                |
| docutils       | 2.59 sec                                               | 2.88 sec: 1.11x slower                                              |
| html5lib       | 64.2 ms                                                | 66.8 ms: 1.04x slower                                               |
| sphinx         | 1.03 sec                                               | 1.15 sec: 1.11x slower                                              |
| Geometric mean | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                |
| async_tree_none            | 351 ms                                                 | 334 ms: 1.05x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 421 ms: 1.05x faster                                                |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 558 ms: 1.02x slower                                                |
| async_tree_io              | 842 ms                                                 | 864 ms: 1.03x slower                                                |
| async_generators           | 436 ms                                                 | 458 ms: 1.05x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 984 ms: 1.15x slower                                                |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, coroutines, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 83.9 ms: 1.04x faster                                               |
| float          | 79.2 ms                                                | 76.4 ms: 1.04x faster                                               |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.3 ms: 1.08x faster                                               |
| regex_effbot   | 3.73 ms                                                | 3.53 ms: 1.06x faster                                               |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                |
| regex_compile  | 132 ms                                                 | 136 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.94 sec: 1.11x faster                                              |
| xml_etree_generate   | 86.7 ms                                                | 78.9 ms: 1.10x faster                                               |
| xml_etree_process    | 60.6 ms                                                | 55.4 ms: 1.09x faster                                               |
| unpickle_pure_python | 216 us                                                 | 198 us: 1.09x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                               |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                               |
| json_dumps           | 10.6 ms                                                | 10.9 ms: 1.03x slower                                               |
| pickle_pure_python   | 310 us                                                 | 322 us: 1.04x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                               |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                               |
| genshi_text     | 23.5 ms                                                | 24.1 ms: 1.03x slower                                               |
| django_template | 35.2 ms                                                | 36.6 ms: 1.04x slower                                               |
| genshi_xml      | 50.9 ms                                                | 56.7 ms: 1.11x slower                                               |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 272 us: 1.32x faster                                                |
| deepcopy_memo              | 39.1 us                                                | 29.8 us: 1.31x faster                                               |
| richards                   | 48.7 ms                                                | 37.9 ms: 1.28x faster                                               |
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                |
| richards_super             | 54.9 ms                                                | 45.3 ms: 1.21x faster                                               |
| deepcopy_reduce            | 3.20 us                                                | 2.75 us: 1.17x faster                                               |
| scimark_fft                | 364 ms                                                 | 318 ms: 1.15x faster                                                |
| telco                      | 8.54 ms                                                | 7.61 ms: 1.12x faster                                               |
| crypto_pyaes               | 75.3 ms                                                | 67.8 ms: 1.11x faster                                               |
| tomli_loads                | 2.14 sec                                               | 1.94 sec: 1.11x faster                                              |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                               |
| xml_etree_generate         | 86.7 ms                                                | 78.9 ms: 1.10x faster                                               |
| go                         | 144 ms                                                 | 131 ms: 1.10x faster                                                |
| xml_etree_process          | 60.6 ms                                                | 55.4 ms: 1.09x faster                                               |
| json                       | 5.36 ms                                                | 4.92 ms: 1.09x faster                                               |
| unpickle_pure_python       | 216 us                                                 | 198 us: 1.09x faster                                                |
| regex_v8                   | 26.2 ms                                                | 24.3 ms: 1.08x faster                                               |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.08x faster                                               |
| pyflate                    | 471 ms                                                 | 441 ms: 1.07x faster                                                |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.74 ms: 1.06x faster                                               |
| bpe_tokeniser              | 4.75 sec                                               | 4.49 sec: 1.06x faster                                              |
| regex_effbot               | 3.73 ms                                                | 3.53 ms: 1.06x faster                                               |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                |
| async_tree_none            | 351 ms                                                 | 334 ms: 1.05x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 421 ms: 1.05x faster                                                |
| fannkuch                   | 404 ms                                                 | 385 ms: 1.05x faster                                                |
| logging_format             | 6.40 us                                                | 6.13 us: 1.04x faster                                               |
| nbody                      | 87.0 ms                                                | 83.9 ms: 1.04x faster                                               |
| float                      | 79.2 ms                                                | 76.4 ms: 1.04x faster                                               |
| thrift                     | 809 us                                                 | 786 us: 1.03x faster                                                |
| logging_silent             | 102 ns                                                 | 98.8 ns: 1.03x faster                                               |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                |
| scimark_sor                | 124 ms                                                 | 121 ms: 1.02x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                               |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.02x faster                                              |
| pprint_safe_repr           | 728 ms                                                 | 716 ms: 1.02x faster                                                |
| connected_components       | 444 ms                                                 | 438 ms: 1.01x faster                                                |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                              |
| json_loads                 | 27.2 us                                                | 26.9 us: 1.01x faster                                               |
| logging_simple             | 5.72 us                                                | 5.65 us: 1.01x faster                                               |
| coverage                   | 84.0 ms                                                | 83.4 ms: 1.01x faster                                               |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                |
| mdp                        | 2.72 sec                                               | 2.73 sec: 1.00x slower                                              |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                |
| 2to3                       | 267 ms                                                 | 269 ms: 1.01x slower                                                |
| deltablue                  | 3.23 ms                                                | 3.26 ms: 1.01x slower                                               |
| chaos                      | 58.1 ms                                                | 58.7 ms: 1.01x slower                                               |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.01x slower                                                |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                               |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 558 ms: 1.02x slower                                                |
| genshi_text                | 23.5 ms                                                | 24.1 ms: 1.03x slower                                               |
| async_tree_io              | 842 ms                                                 | 864 ms: 1.03x slower                                                |
| regex_compile              | 132 ms                                                 | 136 ms: 1.03x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 138 ms: 1.03x slower                                                |
| json_dumps                 | 10.6 ms                                                | 10.9 ms: 1.03x slower                                               |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                               |
| pickle_pure_python         | 310 us                                                 | 322 us: 1.04x slower                                                |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.04x slower                                                |
| html5lib                   | 64.2 ms                                                | 66.8 ms: 1.04x slower                                               |
| django_template            | 35.2 ms                                                | 36.6 ms: 1.04x slower                                               |
| sqlglot_transpile          | 1.58 ms                                                | 1.65 ms: 1.04x slower                                               |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.8 ms: 1.04x slower                                               |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.04x slower                                               |
| gc_traversal               | 4.37 ms                                                | 4.56 ms: 1.04x slower                                               |
| dulwich_log                | 64.3 ms                                                | 67.3 ms: 1.05x slower                                               |
| raytrace                   | 267 ms                                                 | 280 ms: 1.05x slower                                                |
| async_generators           | 436 ms                                                 | 458 ms: 1.05x slower                                                |
| sqlglot_optimize           | 53.7 ms                                                | 57.0 ms: 1.06x slower                                               |
| sqlglot_normalize          | 108 ms                                                 | 114 ms: 1.06x slower                                                |
| bench_thread_pool          | 822 us                                                 | 882 us: 1.07x slower                                                |
| sympy_str                  | 275 ms                                                 | 298 ms: 1.08x slower                                                |
| sympy_expand               | 463 ms                                                 | 503 ms: 1.09x slower                                                |
| sphinx                     | 1.03 sec                                               | 1.15 sec: 1.11x slower                                              |
| docutils                   | 2.59 sec                                               | 2.88 sec: 1.11x slower                                              |
| genshi_xml                 | 50.9 ms                                                | 56.7 ms: 1.11x slower                                               |
| create_gc_cycles           | 2.41 ms                                                | 2.69 ms: 1.12x slower                                               |
| nqueens                    | 78.4 ms                                                | 87.6 ms: 1.12x slower                                               |
| sympy_integrate            | 19.9 ms                                                | 22.3 ms: 1.12x slower                                               |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.13x slower                                                |
| pylint                     | 313 ms                                                 | 353 ms: 1.13x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 984 ms: 1.15x slower                                                |
| hexiom                     | 6.16 ms                                                | 7.27 ms: 1.18x slower                                               |
| generators                 | 29.0 ms                                                | 35.7 ms: 1.23x slower                                               |
| k_core                     | 2.35 sec                                               | 3.66 sec: 1.56x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 79.3 ms: 3.31x slower                                               |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (5): scimark_monte_carlo, async_tree_cpu_io_mixed, coroutines, shortest_path, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241111-3.14.0a1+-aaa9ae0-JIT/bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0.json: sqlite_synth

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 72.28% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x