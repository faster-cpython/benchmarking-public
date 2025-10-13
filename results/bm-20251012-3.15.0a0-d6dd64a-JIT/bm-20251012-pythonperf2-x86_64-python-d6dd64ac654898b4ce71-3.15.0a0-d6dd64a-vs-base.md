# Results vs. base

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: linux-x86_64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.000x slower
- HPT reliability: 52.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 278 ms                                                                                                                | 281 ms: 1.01x slower                                                                                                      |
| docutils       | 2.84 sec                                                                                                              | 2.90 sec: 1.02x slower                                                                                                    |
| html5lib       | 64.0 ms                                                                                                               | 66.6 ms: 1.04x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets         | 387 ms                                                                                                                | 384 ms: 1.01x faster                                                                                                      |
| async_tree_none            | 273 ms                                                                                                                | 272 ms: 1.00x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 508 ms                                                                                                                | 512 ms: 1.01x slower                                                                                                      |
| coroutines                 | 22.1 ms                                                                                                               | 22.6 ms: 1.02x slower                                                                                                     |
| async_generators           | 426 ms                                                                                                                | 442 ms: 1.04x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_memoization, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_tcp, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 68.9 ms                                                                                                               | 67.8 ms: 1.02x faster                                                                                                     |
| nbody          | 89.6 ms                                                                                                               | 103 ms: 1.15x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.04x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 24.3 ms                                                                                                               | 24.2 ms: 1.01x faster                                                                                                     |
| regex_effbot   | 3.32 ms                                                                                                               | 3.30 ms: 1.00x faster                                                                                                     |
| regex_compile  | 131 ms                                                                                                                | 132 ms: 1.01x slower                                                                                                      |
| regex_dna      | 220 ms                                                                                                                | 225 ms: 1.02x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 205 us                                                                                                                | 194 us: 1.06x faster                                                                                                      |
| pickle_dict          | 35.1 us                                                                                                               | 33.5 us: 1.05x faster                                                                                                     |
| tomli_loads          | 1.99 sec                                                                                                              | 1.90 sec: 1.05x faster                                                                                                    |
| xml_etree_process    | 58.0 ms                                                                                                               | 55.5 ms: 1.04x faster                                                                                                     |
| pickle               | 12.7 us                                                                                                               | 12.2 us: 1.04x faster                                                                                                     |
| xml_etree_parse      | 143 ms                                                                                                                | 138 ms: 1.04x faster                                                                                                      |
| xml_etree_generate   | 82.8 ms                                                                                                               | 80.1 ms: 1.03x faster                                                                                                     |
| unpickle_list        | 5.20 us                                                                                                               | 5.07 us: 1.03x faster                                                                                                     |
| xml_etree_iterparse  | 98.8 ms                                                                                                               | 96.5 ms: 1.02x faster                                                                                                     |
| pickle_list          | 5.04 us                                                                                                               | 4.98 us: 1.01x faster                                                                                                     |
| json_dumps           | 10.1 ms                                                                                                               | 10.1 ms: 1.01x faster                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.03x faster                                                                                                              |

Benchmark hidden because not significant (3): pickle_pure_python, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.81 ms                                                                                                               | 8.83 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                                                                               | 9.85 ms: 1.08x faster                                                                                                     |
| django_template | 35.6 ms                                                                                                               | 34.9 ms: 1.02x faster                                                                                                     |
| genshi_xml      | 53.5 ms                                                                                                               | 53.8 ms: 1.00x slower                                                                                                     |
| genshi_text     | 23.0 ms                                                                                                               | 23.2 ms: 1.01x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.02x faster                                                                                                              |

All benchmarks:
===============

| Benchmark                  | results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json | results/bm-20251012-3.15.0a0-d6dd64a-JIT/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| coverage                   | 87.4 ms                                                                                                               | 80.3 ms: 1.09x faster                                                                                                     |
| mako                       | 10.7 ms                                                                                                               | 9.85 ms: 1.08x faster                                                                                                     |
| pprint_pformat             | 1.56 sec                                                                                                              | 1.47 sec: 1.06x faster                                                                                                    |
| pprint_safe_repr           | 769 ms                                                                                                                | 727 ms: 1.06x faster                                                                                                      |
| unpickle_pure_python       | 205 us                                                                                                                | 194 us: 1.06x faster                                                                                                      |
| pickle_dict                | 35.1 us                                                                                                               | 33.5 us: 1.05x faster                                                                                                     |
| tomli_loads                | 1.99 sec                                                                                                              | 1.90 sec: 1.05x faster                                                                                                    |
| xml_etree_process          | 58.0 ms                                                                                                               | 55.5 ms: 1.04x faster                                                                                                     |
| k_core                     | 2.10 sec                                                                                                              | 2.01 sec: 1.04x faster                                                                                                    |
| pickle                     | 12.7 us                                                                                                               | 12.2 us: 1.04x faster                                                                                                     |
| xml_etree_parse            | 143 ms                                                                                                                | 138 ms: 1.04x faster                                                                                                      |
| bpe_tokeniser              | 4.74 sec                                                                                                              | 4.58 sec: 1.04x faster                                                                                                    |
| xml_etree_generate         | 82.8 ms                                                                                                               | 80.1 ms: 1.03x faster                                                                                                     |
| connected_components       | 422 ms                                                                                                                | 409 ms: 1.03x faster                                                                                                      |
| sqlite_synth               | 2.85 us                                                                                                               | 2.77 us: 1.03x faster                                                                                                     |
| deepcopy_reduce            | 2.96 us                                                                                                               | 2.87 us: 1.03x faster                                                                                                     |
| unpickle_list              | 5.20 us                                                                                                               | 5.07 us: 1.03x faster                                                                                                     |
| shortest_path              | 455 ms                                                                                                                | 443 ms: 1.03x faster                                                                                                      |
| pyflate                    | 405 ms                                                                                                                | 395 ms: 1.03x faster                                                                                                      |
| xml_etree_iterparse        | 98.8 ms                                                                                                               | 96.5 ms: 1.02x faster                                                                                                     |
| django_template            | 35.6 ms                                                                                                               | 34.9 ms: 1.02x faster                                                                                                     |
| logging_silent             | 94.1 ns                                                                                                               | 92.4 ns: 1.02x faster                                                                                                     |
| deepcopy                   | 267 us                                                                                                                | 262 us: 1.02x faster                                                                                                      |
| float                      | 68.9 ms                                                                                                               | 67.8 ms: 1.02x faster                                                                                                     |
| scimark_lu                 | 96.1 ms                                                                                                               | 94.6 ms: 1.02x faster                                                                                                     |
| pathlib                    | 15.4 ms                                                                                                               | 15.2 ms: 1.01x faster                                                                                                     |
| pickle_list                | 5.04 us                                                                                                               | 4.98 us: 1.01x faster                                                                                                     |
| scimark_fft                | 276 ms                                                                                                                | 273 ms: 1.01x faster                                                                                                      |
| raytrace                   | 283 ms                                                                                                                | 280 ms: 1.01x faster                                                                                                      |
| asyncio_websockets         | 387 ms                                                                                                                | 384 ms: 1.01x faster                                                                                                      |
| regex_v8                   | 24.3 ms                                                                                                               | 24.2 ms: 1.01x faster                                                                                                     |
| json_dumps                 | 10.1 ms                                                                                                               | 10.1 ms: 1.01x faster                                                                                                     |
| telco                      | 154 ms                                                                                                                | 154 ms: 1.01x faster                                                                                                      |
| regex_effbot               | 3.32 ms                                                                                                               | 3.30 ms: 1.00x faster                                                                                                     |
| mdp                        | 1.27 sec                                                                                                              | 1.27 sec: 1.00x faster                                                                                                    |
| async_tree_none            | 273 ms                                                                                                                | 272 ms: 1.00x faster                                                                                                      |
| subparsers                 | 44.7 ms                                                                                                               | 44.6 ms: 1.00x faster                                                                                                     |
| python_startup_no_site     | 8.81 ms                                                                                                               | 8.83 ms: 1.00x slower                                                                                                     |
| gc_traversal               | 6.49 ms                                                                                                               | 6.51 ms: 1.00x slower                                                                                                     |
| genshi_xml                 | 53.5 ms                                                                                                               | 53.8 ms: 1.00x slower                                                                                                     |
| dulwich_log                | 59.3 ms                                                                                                               | 59.6 ms: 1.01x slower                                                                                                     |
| meteor_contest             | 120 ms                                                                                                                | 121 ms: 1.01x slower                                                                                                      |
| deltablue                  | 3.17 ms                                                                                                               | 3.19 ms: 1.01x slower                                                                                                     |
| regex_compile              | 131 ms                                                                                                                | 132 ms: 1.01x slower                                                                                                      |
| many_optionals             | 1.22 ms                                                                                                               | 1.23 ms: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 508 ms                                                                                                                | 512 ms: 1.01x slower                                                                                                      |
| create_gc_cycles           | 2.87 ms                                                                                                               | 2.90 ms: 1.01x slower                                                                                                     |
| spectral_norm              | 85.4 ms                                                                                                               | 86.2 ms: 1.01x slower                                                                                                     |
| fannkuch                   | 359 ms                                                                                                                | 363 ms: 1.01x slower                                                                                                      |
| 2to3                       | 278 ms                                                                                                                | 281 ms: 1.01x slower                                                                                                      |
| chaos                      | 57.8 ms                                                                                                               | 58.4 ms: 1.01x slower                                                                                                     |
| sqlglot_v2_normalize       | 113 ms                                                                                                                | 115 ms: 1.01x slower                                                                                                      |
| sqlglot_v2_transpile       | 1.67 ms                                                                                                               | 1.69 ms: 1.01x slower                                                                                                     |
| genshi_text                | 23.0 ms                                                                                                               | 23.2 ms: 1.01x slower                                                                                                     |
| sympy_str                  | 286 ms                                                                                                                | 291 ms: 1.02x slower                                                                                                      |
| sqlglot_v2_optimize        | 57.0 ms                                                                                                               | 58.0 ms: 1.02x slower                                                                                                     |
| json                       | 5.34 ms                                                                                                               | 5.44 ms: 1.02x slower                                                                                                     |
| crypto_pyaes               | 75.5 ms                                                                                                               | 76.9 ms: 1.02x slower                                                                                                     |
| sympy_integrate            | 21.8 ms                                                                                                               | 22.2 ms: 1.02x slower                                                                                                     |
| go                         | 117 ms                                                                                                                | 119 ms: 1.02x slower                                                                                                      |
| coroutines                 | 22.1 ms                                                                                                               | 22.6 ms: 1.02x slower                                                                                                     |
| richards                   | 44.4 ms                                                                                                               | 45.3 ms: 1.02x slower                                                                                                     |
| docutils                   | 2.84 sec                                                                                                              | 2.90 sec: 1.02x slower                                                                                                    |
| regex_dna                  | 220 ms                                                                                                                | 225 ms: 1.02x slower                                                                                                      |
| richards_super             | 50.2 ms                                                                                                               | 51.3 ms: 1.02x slower                                                                                                     |
| typing_runtime_protocols   | 166 us                                                                                                                | 171 us: 1.03x slower                                                                                                      |
| hexiom                     | 5.77 ms                                                                                                               | 5.94 ms: 1.03x slower                                                                                                     |
| sympy_expand               | 486 ms                                                                                                                | 502 ms: 1.03x slower                                                                                                      |
| deepcopy_memo              | 25.3 us                                                                                                               | 26.2 us: 1.04x slower                                                                                                     |
| async_generators           | 426 ms                                                                                                                | 442 ms: 1.04x slower                                                                                                      |
| html5lib                   | 64.0 ms                                                                                                               | 66.6 ms: 1.04x slower                                                                                                     |
| scimark_monte_carlo        | 61.0 ms                                                                                                               | 63.9 ms: 1.05x slower                                                                                                     |
| scimark_sparse_mat_mult    | 4.47 ms                                                                                                               | 4.78 ms: 1.07x slower                                                                                                     |
| comprehensions             | 15.9 us                                                                                                               | 17.3 us: 1.09x slower                                                                                                     |
| nbody                      | 89.6 ms                                                                                                               | 103 ms: 1.15x slower                                                                                                      |
| unpack_sequence            | 45.5 ns                                                                                                               | 52.9 ns: 1.16x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (27): async_tree_io_tg, bench_thread_pool, pycparser, generators, async_tree_io, logging_format, scimark_sor, nqueens, async_tree_memoization, pidigits, python_startup, pickle_pure_python, logging_simple, asyncio_tcp_ssl, json_loads, async_tree_cpu_io_mixed, sqlglot_v2_parse, unpickle, async_tree_none_tg, sympy_sum, djangocms, asyncio_tcp, thrift, pylint, async_tree_memoization_tg, sphinx, bench_mp_pool

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 52.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x