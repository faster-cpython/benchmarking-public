# Results vs. base

- fork: python
- ref: 800d37feca2e0ea33439
- machine: windows-amd64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.023x faster
- HPT reliability: 98.36%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                                                                             | 1.64 sec: 1.03x slower                                                                                                   |
| html5lib       | 38.2 ms                                                                                                              | 39.2 ms: 1.03x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 168 ms                                                                                                               | 166 ms: 1.01x faster                                                                                                     |
| async_tree_cpu_io_mixed    | 329 ms                                                                                                               | 332 ms: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed_tg | 333 ms                                                                                                               | 338 ms: 1.01x slower                                                                                                     |
| async_tree_memoization_tg  | 206 ms                                                                                                               | 210 ms: 1.02x slower                                                                                                     |
| asyncio_websockets         | 158 ms                                                                                                               | 163 ms: 1.03x slower                                                                                                     |
| async_generators           | 232 ms                                                                                                               | 243 ms: 1.04x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.27 sec                                                                                                             | 1.42 sec: 1.12x slower                                                                                                   |
| asyncio_tcp                | 400 ms                                                                                                               | 506 ms: 1.26x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.04x slower                                                                                                             |

Benchmark hidden because not significant (5): async_tree_none_tg, coroutines, async_tree_io, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                                                                              | 54.5 ms: 1.20x faster                                                                                                    |
| float          | 42.7 ms                                                                                                              | 43.5 ms: 1.02x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 1.47 ms                                                                                                              | 1.59 ms: 1.08x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmark hidden because not significant (3): regex_dna, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                                                                             | 1.10 sec: 1.27x faster                                                                                                   |
| unpickle_pure_python | 132 us                                                                                                               | 105 us: 1.26x faster                                                                                                     |
| xml_etree_process    | 38.4 ms                                                                                                              | 34.9 ms: 1.10x faster                                                                                                    |
| xml_etree_generate   | 54.9 ms                                                                                                              | 50.2 ms: 1.09x faster                                                                                                    |
| unpickle_list        | 2.95 us                                                                                                              | 2.76 us: 1.07x faster                                                                                                    |
| pickle_list          | 3.42 us                                                                                                              | 3.26 us: 1.05x faster                                                                                                    |
| pickle_pure_python   | 212 us                                                                                                               | 203 us: 1.05x faster                                                                                                     |
| pickle               | 7.85 us                                                                                                              | 7.68 us: 1.02x faster                                                                                                    |
| unpickle             | 8.65 us                                                                                                              | 8.54 us: 1.01x faster                                                                                                    |
| xml_etree_parse      | 88.4 ms                                                                                                              | 87.7 ms: 1.01x faster                                                                                                    |
| json_dumps           | 6.17 ms                                                                                                              | 6.28 ms: 1.02x slower                                                                                                    |
| json_loads           | 14.2 us                                                                                                              | 14.7 us: 1.03x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 19.7 ms                                                                                                              | 19.2 ms: 1.03x faster                                                                                                    |
| python_startup         | 25.7 ms                                                                                                              | 25.0 ms: 1.03x faster                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.44 ms                                                                                                              | 5.32 ms: 1.21x faster                                                                                                    |
| django_template | 24.5 ms                                                                                                              | 24.1 ms: 1.02x faster                                                                                                    |
| genshi_text     | 15.0 ms                                                                                                              | 15.5 ms: 1.03x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.05x faster                                                                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json | results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf1-amd64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| fannkuch                   | 270 ms                                                                                                               | 211 ms: 1.28x faster                                                                                                     |
| tomli_loads                | 1.39 sec                                                                                                             | 1.10 sec: 1.27x faster                                                                                                   |
| unpickle_pure_python       | 132 us                                                                                                               | 105 us: 1.26x faster                                                                                                     |
| scimark_fft                | 189 ms                                                                                                               | 151 ms: 1.25x faster                                                                                                     |
| mako                       | 6.44 ms                                                                                                              | 5.32 ms: 1.21x faster                                                                                                    |
| nbody                      | 65.5 ms                                                                                                              | 54.5 ms: 1.20x faster                                                                                                    |
| bpe_tokeniser              | 2.95 sec                                                                                                             | 2.52 sec: 1.17x faster                                                                                                   |
| pyflate                    | 285 ms                                                                                                               | 251 ms: 1.14x faster                                                                                                     |
| xml_etree_process          | 38.4 ms                                                                                                              | 34.9 ms: 1.10x faster                                                                                                    |
| pprint_pformat             | 1.00 sec                                                                                                             | 911 ms: 1.10x faster                                                                                                     |
| xml_etree_generate         | 54.9 ms                                                                                                              | 50.2 ms: 1.09x faster                                                                                                    |
| unpack_sequence            | 36.3 ns                                                                                                              | 33.3 ns: 1.09x faster                                                                                                    |
| pprint_safe_repr           | 490 ms                                                                                                               | 450 ms: 1.09x faster                                                                                                     |
| scimark_sparse_mat_mult    | 2.48 ms                                                                                                              | 2.28 ms: 1.09x faster                                                                                                    |
| unpickle_list              | 2.95 us                                                                                                              | 2.76 us: 1.07x faster                                                                                                    |
| k_core                     | 1.70 sec                                                                                                             | 1.61 sec: 1.06x faster                                                                                                   |
| telco                      | 4.47 ms                                                                                                              | 4.24 ms: 1.06x faster                                                                                                    |
| crypto_pyaes               | 48.7 ms                                                                                                              | 46.3 ms: 1.05x faster                                                                                                    |
| pickle_list                | 3.42 us                                                                                                              | 3.26 us: 1.05x faster                                                                                                    |
| pickle_pure_python         | 212 us                                                                                                               | 203 us: 1.05x faster                                                                                                     |
| comprehensions             | 10.7 us                                                                                                              | 10.3 us: 1.04x faster                                                                                                    |
| sqlglot_v2_parse           | 815 us                                                                                                               | 783 us: 1.04x faster                                                                                                     |
| nqueens                    | 61.5 ms                                                                                                              | 59.3 ms: 1.04x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.02 ms                                                                                                              | 987 us: 1.03x faster                                                                                                     |
| sqlite_synth               | 1.59 us                                                                                                              | 1.54 us: 1.03x faster                                                                                                    |
| python_startup_no_site     | 19.7 ms                                                                                                              | 19.2 ms: 1.03x faster                                                                                                    |
| gc_traversal               | 2.16 ms                                                                                                              | 2.10 ms: 1.03x faster                                                                                                    |
| python_startup             | 25.7 ms                                                                                                              | 25.0 ms: 1.03x faster                                                                                                    |
| scimark_monte_carlo        | 41.1 ms                                                                                                              | 40.1 ms: 1.02x faster                                                                                                    |
| pickle                     | 7.85 us                                                                                                              | 7.68 us: 1.02x faster                                                                                                    |
| sqlglot_v2_normalize       | 71.9 ms                                                                                                              | 70.4 ms: 1.02x faster                                                                                                    |
| logging_silent             | 55.1 ns                                                                                                              | 54.0 ns: 1.02x faster                                                                                                    |
| meteor_contest             | 71.9 ms                                                                                                              | 70.5 ms: 1.02x faster                                                                                                    |
| django_template            | 24.5 ms                                                                                                              | 24.1 ms: 1.02x faster                                                                                                    |
| shortest_path              | 360 ms                                                                                                               | 354 ms: 1.02x faster                                                                                                     |
| connected_components       | 330 ms                                                                                                               | 324 ms: 1.02x faster                                                                                                     |
| go                         | 77.0 ms                                                                                                              | 75.7 ms: 1.02x faster                                                                                                    |
| chaos                      | 40.9 ms                                                                                                              | 40.3 ms: 1.01x faster                                                                                                    |
| unpickle                   | 8.65 us                                                                                                              | 8.54 us: 1.01x faster                                                                                                    |
| hexiom                     | 4.03 ms                                                                                                              | 3.98 ms: 1.01x faster                                                                                                    |
| create_gc_cycles           | 1.33 ms                                                                                                              | 1.31 ms: 1.01x faster                                                                                                    |
| async_tree_none            | 168 ms                                                                                                               | 166 ms: 1.01x faster                                                                                                     |
| spectral_norm              | 65.6 ms                                                                                                              | 64.9 ms: 1.01x faster                                                                                                    |
| xml_etree_parse            | 88.4 ms                                                                                                              | 87.7 ms: 1.01x faster                                                                                                    |
| coverage                   | 49.6 ms                                                                                                              | 49.4 ms: 1.01x faster                                                                                                    |
| async_tree_cpu_io_mixed    | 329 ms                                                                                                               | 332 ms: 1.01x slower                                                                                                     |
| deltablue                  | 2.17 ms                                                                                                              | 2.19 ms: 1.01x slower                                                                                                    |
| deepcopy_reduce            | 1.80 us                                                                                                              | 1.82 us: 1.01x slower                                                                                                    |
| logging_format             | 6.46 us                                                                                                              | 6.54 us: 1.01x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 333 ms                                                                                                               | 338 ms: 1.01x slower                                                                                                     |
| scimark_lu                 | 58.3 ms                                                                                                              | 59.2 ms: 1.02x slower                                                                                                    |
| deepcopy                   | 167 us                                                                                                               | 170 us: 1.02x slower                                                                                                     |
| json_dumps                 | 6.17 ms                                                                                                              | 6.28 ms: 1.02x slower                                                                                                    |
| async_tree_memoization_tg  | 206 ms                                                                                                               | 210 ms: 1.02x slower                                                                                                     |
| float                      | 42.7 ms                                                                                                              | 43.5 ms: 1.02x slower                                                                                                    |
| sympy_expand               | 284 ms                                                                                                               | 290 ms: 1.02x slower                                                                                                     |
| generators                 | 19.4 ms                                                                                                              | 19.8 ms: 1.02x slower                                                                                                    |
| many_optionals             | 435 us                                                                                                               | 446 us: 1.03x slower                                                                                                     |
| html5lib                   | 38.2 ms                                                                                                              | 39.2 ms: 1.03x slower                                                                                                    |
| docutils                   | 1.60 sec                                                                                                             | 1.64 sec: 1.03x slower                                                                                                   |
| richards_super             | 31.0 ms                                                                                                              | 31.8 ms: 1.03x slower                                                                                                    |
| genshi_text                | 15.0 ms                                                                                                              | 15.5 ms: 1.03x slower                                                                                                    |
| deepcopy_memo              | 17.5 us                                                                                                              | 18.0 us: 1.03x slower                                                                                                    |
| asyncio_websockets         | 158 ms                                                                                                               | 163 ms: 1.03x slower                                                                                                     |
| json_loads                 | 14.2 us                                                                                                              | 14.7 us: 1.03x slower                                                                                                    |
| json                       | 2.99 ms                                                                                                              | 3.09 ms: 1.04x slower                                                                                                    |
| sympy_integrate            | 12.3 ms                                                                                                              | 12.7 ms: 1.04x slower                                                                                                    |
| async_generators           | 232 ms                                                                                                               | 243 ms: 1.04x slower                                                                                                     |
| richards                   | 26.8 ms                                                                                                              | 28.1 ms: 1.05x slower                                                                                                    |
| regex_effbot               | 1.47 ms                                                                                                              | 1.59 ms: 1.08x slower                                                                                                    |
| asyncio_tcp_ssl            | 1.27 sec                                                                                                             | 1.42 sec: 1.12x slower                                                                                                   |
| asyncio_tcp                | 400 ms                                                                                                               | 506 ms: 1.26x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmark hidden because not significant (30): pickle_dict, pathlib, async_tree_none_tg, typing_runtime_protocols, pycparser, scimark_sor, bench_mp_pool, coroutines, pidigits, mdp, dulwich_log, regex_dna, sympy_sum, raytrace, async_tree_io, logging_simple, sphinx, regex_compile, async_tree_memoization, xml_etree_iterparse, sympy_str, 2to3, sqlglot_v2_optimize, genshi_xml, subparsers, regex_v8, async_tree_io_tg, thrift, pylint, bench_thread_pool

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 98.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown