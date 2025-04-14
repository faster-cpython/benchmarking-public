# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_warmup_aggressiv
- machine: linux-x86_64
- commit hash: f3b01c5
- commit date: 2025-03-05
- overall geometric mean: 1.032x faster
- HPT reliability: 90.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 273 ms: 1.03x slower                                                         |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.05x slower                                                       |
| html5lib       | 63.4 ms                                                | 62.5 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 628 ms: 1.37x faster                                                         |
| async_tree_io              | 838 ms                                                 | 618 ms: 1.36x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 330 ms: 1.32x faster                                                         |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                         |
| async_generators           | 433 ms                                                 | 411 ms: 1.06x faster                                                         |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                         |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.7 ms: 1.13x faster                                                        |
| nbody          | 87.7 ms                                                | 89.1 ms: 1.02x slower                                                        |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.34 ms: 1.13x faster                                                        |
| regex_v8       | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                        |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 79.4 ms: 1.09x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 56.1 ms: 1.08x faster                                                        |
| xml_etree_parse      | 154 ms                                                 | 147 ms: 1.05x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 99.6 ms: 1.02x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 210 us: 1.01x faster                                                         |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                                         |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.15 ms: 1.02x slower                                                        |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                        |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                        |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 628 ms: 1.37x faster                                                         |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                         |
| async_tree_io              | 838 ms                                                 | 618 ms: 1.36x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 330 ms: 1.32x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.32x faster                                                        |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                         |
| scimark_fft                | 367 ms                                                 | 314 ms: 1.17x faster                                                         |
| go                         | 141 ms                                                 | 122 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                         |
| float                      | 78.7 ms                                                | 69.7 ms: 1.13x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.34 ms: 1.13x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.48 ms: 1.12x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                       |
| telco                      | 8.40 ms                                                | 7.54 ms: 1.11x faster                                                        |
| spectral_norm              | 113 ms                                                 | 102 ms: 1.11x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 79.4 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 56.1 ms: 1.08x faster                                                        |
| pylint                     | 312 ms                                                 | 289 ms: 1.08x faster                                                         |
| richards                   | 47.5 ms                                                | 44.2 ms: 1.08x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                        |
| thrift                     | 800 us                                                 | 753 us: 1.06x faster                                                         |
| richards_super             | 53.7 ms                                                | 50.6 ms: 1.06x faster                                                        |
| async_generators           | 433 ms                                                 | 411 ms: 1.06x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 147 ms: 1.05x faster                                                         |
| pyflate                    | 470 ms                                                 | 447 ms: 1.05x faster                                                         |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.73 ms: 1.04x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                       |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                       |
| logging_simple             | 5.65 us                                                | 5.52 us: 1.02x faster                                                        |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                        |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                                       |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 99.6 ms: 1.02x faster                                                        |
| html5lib                   | 63.4 ms                                                | 62.5 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 210 us: 1.01x faster                                                         |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                        |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                                         |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.45 ms: 1.00x slower                                                        |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                         |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                         |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 736 ms: 1.01x slower                                                         |
| nbody                      | 87.7 ms                                                | 89.1 ms: 1.02x slower                                                        |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                         |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.02x slower                                                         |
| sympy_str                  | 273 ms                                                 | 278 ms: 1.02x slower                                                         |
| coverage                   | 82.8 ms                                                | 84.4 ms: 1.02x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.15 ms: 1.02x slower                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                         |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                        |
| nqueens                    | 80.9 ms                                                | 82.9 ms: 1.03x slower                                                        |
| 2to3                       | 266 ms                                                 | 273 ms: 1.03x slower                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 68.7 ms: 1.03x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.30 ms: 1.03x slower                                                        |
| chaos                      | 58.0 ms                                                | 59.7 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 53.4 ms                                                | 55.3 ms: 1.04x slower                                                        |
| sympy_expand               | 456 ms                                                 | 474 ms: 1.04x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.04x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 67.3 ms: 1.04x slower                                                        |
| deltablue                  | 3.19 ms                                                | 3.34 ms: 1.04x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.05x slower                                                       |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                         |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                                         |
| sympy_integrate            | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 158 ms: 1.05x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 140 ms: 1.05x slower                                                         |
| logging_silent             | 101 ns                                                 | 107 ns: 1.05x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.56 sec: 1.06x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.43 ms: 1.06x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 890 us: 1.09x slower                                                         |
| comprehensions             | 16.5 us                                                | 18.1 us: 1.10x slower                                                        |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                        |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                        |
| many_optionals             | 857 us                                                 | 993 us: 1.16x slower                                                         |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 87.3 ms: 3.64x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (4): sphinx, regex_compile, json, crypto_pyaes
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 90.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x