# Results vs. 3.13.0

- fork: brandtbucher
- ref: f2b86f10e60051aa48d5
- machine: linux-x86_64
- commit hash: f2b86f1
- commit date: 2025-01-14
- overall geometric mean: 1.031x faster
- HPT reliability: 97.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                         |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 593 ms: 1.45x faster                                                         |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                         |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.32x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 472 ms: 1.15x faster                                                         |
| async_generators           | 433 ms                                                 | 405 ms: 1.07x faster                                                         |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.2 ms: 1.11x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 87.7 ms                                                | 96.4 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.96 ms: 1.27x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                        |
| regex_dna      | 220 ms                                                 | 196 ms: 1.12x faster                                                         |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 78.2 ms: 1.11x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 94.9 ms: 1.07x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                         |
| json_loads           | 27.2 us                                                | 29.5 us: 1.09x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.92 ms: 1.08x faster                                                        |
| genshi_text     | 22.6 ms                                                | 23.6 ms: 1.04x slower                                                        |
| django_template | 31.7 ms                                                | 33.4 ms: 1.05x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 57.4 ms: 1.14x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 593 ms: 1.45x faster                                                         |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                         |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.32x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                         |
| deepcopy                   | 354 us                                                 | 271 us: 1.31x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 30.0 us: 1.28x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 2.96 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 497 ms: 1.15x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 472 ms: 1.15x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| regex_dna                  | 220 ms                                                 | 196 ms: 1.12x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 78.2 ms: 1.11x faster                                                        |
| float                      | 78.7 ms                                                | 71.2 ms: 1.11x faster                                                        |
| scimark_fft                | 367 ms                                                 | 333 ms: 1.10x faster                                                         |
| telco                      | 8.40 ms                                                | 7.65 ms: 1.10x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                                         |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                        |
| pylint                     | 312 ms                                                 | 287 ms: 1.09x faster                                                         |
| richards_super             | 53.7 ms                                                | 49.8 ms: 1.08x faster                                                        |
| mako                       | 10.7 ms                                                | 9.92 ms: 1.08x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.55 ms: 1.08x faster                                                        |
| async_generators           | 433 ms                                                 | 405 ms: 1.07x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 94.9 ms: 1.07x faster                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 62.8 ms: 1.06x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                        |
| crypto_pyaes               | 74.7 ms                                                | 70.7 ms: 1.06x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.78 ms: 1.05x faster                                                        |
| pyflate                    | 470 ms                                                 | 449 ms: 1.05x faster                                                         |
| go                         | 141 ms                                                 | 135 ms: 1.04x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                       |
| thrift                     | 800 us                                                 | 775 us: 1.03x faster                                                         |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                         |
| connected_components       | 447 ms                                                 | 434 ms: 1.03x faster                                                         |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                         |
| json                       | 5.32 ms                                                | 5.22 ms: 1.02x faster                                                        |
| scimark_lu                 | 114 ms                                                 | 112 ms: 1.02x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                       |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                         |
| fannkuch                   | 394 ms                                                 | 388 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.01x slower                                                        |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 733 ms: 1.01x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| mdp                        | 2.54 sec                                               | 2.59 sec: 1.02x slower                                                       |
| logging_simple             | 5.65 us                                                | 5.76 us: 1.02x slower                                                        |
| deltablue                  | 3.19 ms                                                | 3.26 ms: 1.02x slower                                                        |
| logging_format             | 6.23 us                                                | 6.38 us: 1.02x slower                                                        |
| sympy_str                  | 273 ms                                                 | 280 ms: 1.02x slower                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 54.7 ms: 1.03x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                         |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.04x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                         |
| sympy_integrate            | 19.8 ms                                                | 20.6 ms: 1.04x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| genshi_text                | 22.6 ms                                                | 23.6 ms: 1.04x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 67.6 ms: 1.05x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                        |
| django_template            | 31.7 ms                                                | 33.4 ms: 1.05x slower                                                        |
| spectral_norm              | 113 ms                                                 | 120 ms: 1.06x slower                                                         |
| chaos                      | 58.0 ms                                                | 62.8 ms: 1.08x slower                                                        |
| json_loads                 | 27.2 us                                                | 29.5 us: 1.09x slower                                                        |
| logging_silent             | 101 ns                                                 | 110 ns: 1.09x slower                                                         |
| coroutines                 | 22.2 ms                                                | 24.2 ms: 1.09x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 896 us: 1.10x slower                                                         |
| nbody                      | 87.7 ms                                                | 96.4 ms: 1.10x slower                                                        |
| coverage                   | 82.8 ms                                                | 91.8 ms: 1.11x slower                                                        |
| nqueens                    | 80.9 ms                                                | 90.9 ms: 1.12x slower                                                        |
| many_optionals             | 857 us                                                 | 970 us: 1.13x slower                                                         |
| genshi_xml                 | 50.5 ms                                                | 57.4 ms: 1.14x slower                                                        |
| raytrace                   | 262 ms                                                 | 298 ms: 1.14x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                        |
| hexiom                     | 6.08 ms                                                | 7.13 ms: 1.17x slower                                                        |
| generators                 | 28.8 ms                                                | 37.3 ms: 1.30x slower                                                        |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (3): asyncio_websockets, html5lib, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 97.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x