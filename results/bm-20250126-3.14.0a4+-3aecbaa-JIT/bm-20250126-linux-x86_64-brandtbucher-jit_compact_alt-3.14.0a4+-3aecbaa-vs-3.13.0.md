# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_compact_alt
- machine: linux-x86_64
- commit hash: 3aecbaa
- commit date: 2025-01-26
- overall geometric mean: 1.005x faster
- HPT reliability: 84.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 263 ms: 1.01x faster                                                    |
| docutils       | 2.58 sec                                               | 2.83 sec: 1.09x slower                                                  |
| html5lib       | 63.4 ms                                                | 65.4 ms: 1.03x slower                                                   |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 326 ms: 1.42x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 625 ms: 1.38x faster                                                    |
| async_tree_io              | 838 ms                                                 | 637 ms: 1.32x faster                                                    |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 338 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 262 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                    |
| async_generators           | 433 ms                                                 | 396 ms: 1.09x faster                                                    |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                    |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| nbody          | 87.7 ms                                                | 92.9 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                   |
| regex_v8       | 26.9 ms                                                | 24.3 ms: 1.10x faster                                                   |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                    |
| regex_compile  | 132 ms                                                 | 133 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                    |
| tomli_loads          | 2.12 sec                                               | 1.90 sec: 1.12x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 95.7 ms: 1.06x faster                                                   |
| xml_etree_process    | 60.5 ms                                                | 59.7 ms: 1.01x faster                                                   |
| json_loads           | 27.2 us                                                | 29.2 us: 1.08x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 332 us: 1.10x slower                                                    |
| unpickle_pure_python | 213 us                                                 | 237 us: 1.11x slower                                                    |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.18x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                   |
| python_startup_no_site | 7.00 ms                                                | 7.33 ms: 1.05x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.4 ms: 1.03x faster                                                   |
| genshi_xml      | 50.5 ms                                                | 51.0 ms: 1.01x slower                                                   |
| genshi_text     | 22.6 ms                                                | 23.2 ms: 1.03x slower                                                   |
| django_template | 31.7 ms                                                | 34.7 ms: 1.10x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250126-linux-x86_64-brandtbucher-jit_compact_alt-3.14.0a4+-3aecbaa |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 326 ms: 1.42x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 625 ms: 1.38x faster                                                    |
| async_tree_io              | 838 ms                                                 | 637 ms: 1.32x faster                                                    |
| deepcopy                   | 354 us                                                 | 270 us: 1.31x faster                                                    |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                   |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 338 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 262 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 2.77 us: 1.17x faster                                                   |
| float                      | 78.7 ms                                                | 67.6 ms: 1.16x faster                                                   |
| richards                   | 47.5 ms                                                | 41.1 ms: 1.16x faster                                                   |
| scimark_fft                | 367 ms                                                 | 318 ms: 1.15x faster                                                    |
| regex_effbot               | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                   |
| richards_super             | 53.7 ms                                                | 46.9 ms: 1.14x faster                                                   |
| spectral_norm              | 113 ms                                                 | 99.0 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.90 sec: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 24.3 ms: 1.10x faster                                                   |
| async_generators           | 433 ms                                                 | 396 ms: 1.09x faster                                                    |
| xml_etree_generate         | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 69.0 ms: 1.08x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                   |
| telco                      | 8.40 ms                                                | 7.86 ms: 1.07x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.72 ms: 1.07x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.61 ms: 1.06x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 95.7 ms: 1.06x faster                                                   |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                   |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                    |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 64.1 ms: 1.04x faster                                                   |
| pyflate                    | 470 ms                                                 | 451 ms: 1.04x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                  |
| connected_components       | 447 ms                                                 | 433 ms: 1.03x faster                                                    |
| shortest_path              | 487 ms                                                 | 474 ms: 1.03x faster                                                    |
| mako                       | 10.7 ms                                                | 10.4 ms: 1.03x faster                                                   |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 59.7 ms: 1.01x faster                                                   |
| 2to3                       | 266 ms                                                 | 263 ms: 1.01x faster                                                    |
| mdp                        | 2.54 sec                                               | 2.52 sec: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| hexiom                     | 6.08 ms                                                | 6.06 ms: 1.00x faster                                                   |
| nqueens                    | 80.9 ms                                                | 81.2 ms: 1.00x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                   |
| regex_compile              | 132 ms                                                 | 133 ms: 1.01x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                    |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                   |
| genshi_xml                 | 50.5 ms                                                | 51.0 ms: 1.01x slower                                                   |
| chaos                      | 58.0 ms                                                | 58.7 ms: 1.01x slower                                                   |
| go                         | 141 ms                                                 | 143 ms: 1.01x slower                                                    |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                    |
| genshi_text                | 22.6 ms                                                | 23.2 ms: 1.03x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                   |
| thrift                     | 800 us                                                 | 824 us: 1.03x slower                                                    |
| fannkuch                   | 394 ms                                                 | 406 ms: 1.03x slower                                                    |
| html5lib                   | 63.4 ms                                                | 65.4 ms: 1.03x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 750 ms: 1.03x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.03x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.32 ms: 1.04x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                                    |
| python_startup_no_site     | 7.00 ms                                                | 7.33 ms: 1.05x slower                                                   |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                    |
| deltablue                  | 3.19 ms                                                | 3.38 ms: 1.06x slower                                                   |
| nbody                      | 87.7 ms                                                | 92.9 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 56.8 ms: 1.06x slower                                                   |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.07x slower                                                  |
| sympy_expand               | 456 ms                                                 | 489 ms: 1.07x slower                                                    |
| sympy_str                  | 273 ms                                                 | 292 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 160 us                                                 | 172 us: 1.07x slower                                                    |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.08x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.2 us: 1.08x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.83 sec: 1.09x slower                                                  |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                                   |
| django_template            | 31.7 ms                                                | 34.7 ms: 1.10x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 332 us: 1.10x slower                                                    |
| raytrace                   | 262 ms                                                 | 290 ms: 1.11x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 237 us: 1.11x slower                                                    |
| coverage                   | 82.8 ms                                                | 92.5 ms: 1.12x slower                                                   |
| pylint                     | 312 ms                                                 | 353 ms: 1.13x slower                                                    |
| sympy_integrate            | 19.8 ms                                                | 23.1 ms: 1.17x slower                                                   |
| dulwich_log                | 64.6 ms                                                | 75.6 ms: 1.17x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.18x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 178 ms: 1.18x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 972 us: 1.19x slower                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 166 ms: 1.25x slower                                                    |
| many_optionals             | 857 us                                                 | 1.07 ms: 1.25x slower                                                   |
| logging_format             | 6.23 us                                                | 7.87 us: 1.26x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 21.6 ms: 1.28x slower                                                   |
| logging_simple             | 5.65 us                                                | 7.26 us: 1.28x slower                                                   |
| generators                 | 28.8 ms                                                | 38.5 ms: 1.34x slower                                                   |
| subparsers                 | 15.5 ms                                                | 22.6 ms: 1.47x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 90.2 ms: 3.76x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): json
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 84.34% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.16x