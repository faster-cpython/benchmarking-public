# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_threshold_64
- machine: linux-x86_64
- commit hash: 539b80a
- commit date: 2025-06-23
- overall geometric mean: 1.047x faster
- HPT reliability: 97.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 270 ms: 1.02x slower                                                    |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                  |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                    |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 635 ms: 1.35x faster                                                    |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                    |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                                    |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.6 ms: 1.20x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| nbody          | 87.7 ms                                                | 90.9 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                   |
| regex_effbot   | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                   |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.12x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                    |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 80.6 ms: 1.08x faster                                                   |
| unpickle_pure_python | 213 us                                                 | 199 us: 1.07x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                                   |
| json_loads           | 27.2 us                                                | 27.8 us: 1.02x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                                    |
| json_dumps           | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.03x faster                                                   |
| python_startup_no_site | 7.00 ms                                                | 6.97 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                   |
| genshi_xml      | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                   |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                   |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.05x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                                    |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                                    |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 635 ms: 1.35x faster                                                    |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                    |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.30x faster                                                   |
| richards                   | 47.5 ms                                                | 36.9 ms: 1.29x faster                                                   |
| richards_super             | 53.7 ms                                                | 42.0 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                    |
| float                      | 78.7 ms                                                | 65.6 ms: 1.20x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                    |
| go                         | 141 ms                                                 | 122 ms: 1.15x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.12x faster                                                  |
| scimark_fft                | 367 ms                                                 | 328 ms: 1.12x faster                                                    |
| pyflate                    | 470 ms                                                 | 421 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                    |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                    |
| regex_effbot               | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                    |
| dulwich_log                | 64.6 ms                                                | 59.2 ms: 1.09x faster                                                   |
| telco                      | 8.40 ms                                                | 7.74 ms: 1.09x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                   |
| pylint                     | 312 ms                                                 | 289 ms: 1.08x faster                                                    |
| xml_etree_generate         | 86.8 ms                                                | 80.6 ms: 1.08x faster                                                   |
| unpickle_pure_python       | 213 us                                                 | 199 us: 1.07x faster                                                    |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                  |
| thrift                     | 800 us                                                 | 770 us: 1.04x faster                                                    |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.85 ms: 1.04x faster                                                   |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.03x faster                                                   |
| json                       | 5.32 ms                                                | 5.15 ms: 1.03x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                                   |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                    |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                   |
| async_generators           | 433 ms                                                 | 429 ms: 1.01x faster                                                    |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                   |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                    |
| python_startup_no_site     | 7.00 ms                                                | 6.97 ms: 1.01x faster                                                   |
| deltablue                  | 3.19 ms                                                | 3.18 ms: 1.00x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                                   |
| gc_traversal               | 4.90 ms                                                | 4.97 ms: 1.02x slower                                                   |
| 2to3                       | 266 ms                                                 | 270 ms: 1.02x slower                                                    |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                   |
| shortest_path              | 487 ms                                                 | 497 ms: 1.02x slower                                                    |
| json_loads                 | 27.2 us                                                | 27.8 us: 1.02x slower                                                   |
| nqueens                    | 80.9 ms                                                | 82.9 ms: 1.02x slower                                                   |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                   |
| sympy_expand               | 456 ms                                                 | 470 ms: 1.03x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                    |
| djangocms                  | 22.3 us                                                | 23.1 us: 1.04x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                  |
| nbody                      | 87.7 ms                                                | 90.9 ms: 1.04x slower                                                   |
| fannkuch                   | 394 ms                                                 | 408 ms: 1.04x slower                                                    |
| connected_components       | 447 ms                                                 | 467 ms: 1.04x slower                                                    |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                                    |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                    |
| generators                 | 28.8 ms                                                | 30.5 ms: 1.06x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.61 ms: 1.07x slower                                                   |
| coverage                   | 82.8 ms                                                | 88.4 ms: 1.07x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                   |
| chaos                      | 58.0 ms                                                | 62.2 ms: 1.07x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.53 ms: 1.07x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.60 sec: 1.08x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.18 us: 1.09x slower                                                   |
| logging_format             | 6.23 us                                                | 6.94 us: 1.11x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 816 ms: 1.12x slower                                                    |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                   |
| many_optionals             | 857 us                                                 | 1.01 ms: 1.18x slower                                                   |
| subparsers                 | 15.5 ms                                                | 23.5 ms: 1.52x slower                                                   |
| logging_silent             | 101 ns                                                 | 477 ns: 4.72x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (7): sphinx, regex_dna, crypto_pyaes, scimark_sor, scimark_monte_carlo, asyncio_websockets, sympy_str
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250623-3.15.0a0-539b80a-JIT/bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 97.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x