# Results vs. 3.13.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: linux-x86_64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.068x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                  |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                  |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 641 ms: 1.34x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 494 ms: 1.10x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.3 ms: 1.20x faster                                                 |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| nbody          | 87.7 ms                                                | 93.4 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 21.9 ms: 1.23x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.18 ms: 1.18x faster                                                 |
| regex_dna      | 220 ms                                                 | 202 ms: 1.09x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                |
| unpickle_pure_python | 213 us                                                 | 193 us: 1.11x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 55.6 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                                 |
| json_loads           | 27.2 us                                                | 28.1 us: 1.04x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                 |
| mako            | 10.7 ms                                                | 10.5 ms: 1.02x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                 |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.06x faster                                                |
| richards                   | 47.5 ms                                                | 32.2 ms: 1.48x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                  |
| richards_super             | 53.7 ms                                                | 37.9 ms: 1.42x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                  |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                                  |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 641 ms: 1.34x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                  |
| spectral_norm              | 113 ms                                                 | 92.2 ms: 1.23x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 21.9 ms: 1.23x faster                                                 |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                 |
| float                      | 78.7 ms                                                | 65.3 ms: 1.20x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.18 ms: 1.18x faster                                                 |
| scimark_fft                | 367 ms                                                 | 311 ms: 1.18x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                  |
| pyflate                    | 470 ms                                                 | 418 ms: 1.12x faster                                                  |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 193 us: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 494 ms: 1.10x faster                                                  |
| telco                      | 8.40 ms                                                | 7.65 ms: 1.10x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                 |
| regex_dna                  | 220 ms                                                 | 202 ms: 1.09x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.3 ms: 1.09x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 55.6 ms: 1.09x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.33 sec: 1.08x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                 |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                 |
| thrift                     | 800 us                                                 | 774 us: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                 |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                  |
| json                       | 5.32 ms                                                | 5.17 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.90 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 65.2 ms: 1.02x faster                                                 |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| pprint_safe_repr           | 727 ms                                                 | 712 ms: 1.02x faster                                                  |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.02x faster                                                 |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 50.1 ms: 1.01x faster                                                 |
| logging_simple             | 5.65 us                                                | 5.61 us: 1.01x faster                                                 |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.00x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                  |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                  |
| shortest_path              | 487 ms                                                 | 492 ms: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.01x slower                                                |
| nqueens                    | 80.9 ms                                                | 82.1 ms: 1.02x slower                                                 |
| fannkuch                   | 394 ms                                                 | 400 ms: 1.02x slower                                                  |
| connected_components       | 447 ms                                                 | 456 ms: 1.02x slower                                                  |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                  |
| chaos                      | 58.0 ms                                                | 60.1 ms: 1.04x slower                                                 |
| json_loads                 | 27.2 us                                                | 28.1 us: 1.04x slower                                                 |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                                  |
| generators                 | 28.8 ms                                                | 30.2 ms: 1.05x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                  |
| coverage                   | 82.8 ms                                                | 87.2 ms: 1.05x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                  |
| nbody                      | 87.7 ms                                                | 93.4 ms: 1.06x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                 |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.13x slower                                                 |
| many_optionals             | 857 us                                                 | 973 us: 1.14x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.7 ms: 1.53x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (6): sympy_str, async_generators, logging_silent, djangocms, logging_format, crypto_pyaes
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x