# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_warmup_2048
- machine: linux-x86_64
- commit hash: 004e970
- commit date: 2025-03-03
- overall geometric mean: 1.044x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.02x faster                                                    |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                  |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.04x faster                                                   |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.37x faster                                                    |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                    |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 486 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                    |
| async_generators           | 433 ms                                                 | 407 ms: 1.07x faster                                                    |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.6 ms: 1.13x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| nbody          | 87.7 ms                                                | 94.1 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.35 ms: 1.12x faster                                                   |
| regex_v8       | 26.9 ms                                                | 25.6 ms: 1.05x faster                                                   |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 78.2 ms: 1.11x faster                                                   |
| xml_etree_process    | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                   |
| xml_etree_parse      | 154 ms                                                 | 147 ms: 1.05x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 204 us: 1.05x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 99.2 ms: 1.02x faster                                                   |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                    |
| json_loads           | 27.2 us                                                | 29.9 us: 1.10x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.16 ms: 1.02x slower                                                   |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                   |
| mako            | 10.7 ms                                                | 10.2 ms: 1.04x faster                                                   |
| genshi_xml      | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                   |
| django_template | 31.7 ms                                                | 31.5 ms: 1.00x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250303-linux-x86_64-brandtbucher-jit_warmup_2048-3.14.0a5+-004e970 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                    |
| deepcopy                   | 354 us                                                 | 258 us: 1.38x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.37x faster                                                    |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                    |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 2.63 us: 1.23x faster                                                   |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                    |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 486 ms: 1.18x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                  |
| spectral_norm              | 113 ms                                                 | 99.1 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                    |
| float                      | 78.7 ms                                                | 69.6 ms: 1.13x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.35 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.48 ms: 1.12x faster                                                   |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                    |
| xml_etree_generate         | 86.8 ms                                                | 78.2 ms: 1.11x faster                                                   |
| telco                      | 8.40 ms                                                | 7.59 ms: 1.11x faster                                                   |
| pyflate                    | 470 ms                                                 | 426 ms: 1.10x faster                                                    |
| richards                   | 47.5 ms                                                | 43.5 ms: 1.09x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                                   |
| richards_super             | 53.7 ms                                                | 50.2 ms: 1.07x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                   |
| async_generators           | 433 ms                                                 | 407 ms: 1.07x faster                                                    |
| thrift                     | 800 us                                                 | 752 us: 1.06x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.44 sec: 1.06x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 147 ms: 1.05x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 25.6 ms: 1.05x faster                                                   |
| unpickle_pure_python       | 213 us                                                 | 204 us: 1.05x faster                                                    |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.04x faster                                                   |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                    |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 71.9 ms: 1.04x faster                                                   |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.04x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.77 ms: 1.03x faster                                                   |
| shortest_path              | 487 ms                                                 | 475 ms: 1.02x faster                                                    |
| 2to3                       | 266 ms                                                 | 259 ms: 1.02x faster                                                    |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                    |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.53 us: 1.02x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 99.2 ms: 1.02x faster                                                   |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                   |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                    |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                                   |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                  |
| logging_format             | 6.23 us                                                | 6.14 us: 1.02x faster                                                   |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.42 ms: 1.01x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                    |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.00x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                                    |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                    |
| scimark_monte_carlo        | 66.8 ms                                                | 67.9 ms: 1.02x slower                                                   |
| coverage                   | 82.8 ms                                                | 84.2 ms: 1.02x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                   |
| sympy_integrate            | 19.8 ms                                                | 20.3 ms: 1.02x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 7.16 ms: 1.02x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 744 ms: 1.02x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                   |
| chaos                      | 58.0 ms                                                | 59.7 ms: 1.03x slower                                                   |
| fannkuch                   | 394 ms                                                 | 405 ms: 1.03x slower                                                    |
| deltablue                  | 3.19 ms                                                | 3.29 ms: 1.03x slower                                                   |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                                    |
| sympy_expand               | 456 ms                                                 | 471 ms: 1.03x slower                                                    |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 67.2 ms: 1.04x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.36 ms: 1.05x slower                                                   |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                                    |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                    |
| nbody                      | 87.7 ms                                                | 94.1 ms: 1.07x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 879 us: 1.07x slower                                                    |
| comprehensions             | 16.5 us                                                | 17.8 us: 1.08x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.9 us: 1.10x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                   |
| many_optionals             | 857 us                                                 | 971 us: 1.13x slower                                                    |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.43x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (10): meteor_contest, sqlalchemy_imperative, regex_dna, mdp, typing_runtime_protocols, sqlglot_optimize, asyncio_websockets, nqueens, json, sympy_str
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x