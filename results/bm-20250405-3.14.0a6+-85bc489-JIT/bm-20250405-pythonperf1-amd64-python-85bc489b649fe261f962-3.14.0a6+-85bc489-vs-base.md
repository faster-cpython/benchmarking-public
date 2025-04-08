# Results vs. base

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.002x slower
- HPT reliability: 97.10%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                                                                 | 222 ms: 1.01x slower                                                                                                       |
| docutils       | 1.64 sec                                                                                                               | 1.70 sec: 1.04x slower                                                                                                     |
| html5lib       | 38.2 ms                                                                                                                | 38.9 ms: 1.02x slower                                                                                                      |
| sphinx         | 638 ms                                                                                                                 | 653 ms: 1.02x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|--------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets | 157 ms                                                                                                                 | 160 ms: 1.02x slower                                                                                                       |
| coroutines         | 13.5 ms                                                                                                                | 14.2 ms: 1.06x slower                                                                                                      |
| async_generators   | 224 ms                                                                                                                 | 248 ms: 1.11x slower                                                                                                       |
| Geometric mean     | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_memoization_tg, asyncio_tcp, async_tree_none, async_tree_memoization, async_tree_io_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 62.6 ms                                                                                                                | 57.0 ms: 1.10x faster                                                                                                      |
| float          | 42.2 ms                                                                                                                | 43.3 ms: 1.03x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.02x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                                                                                 | 116 ms: 1.02x faster                                                                                                       |
| regex_effbot   | 1.45 ms                                                                                                                | 1.47 ms: 1.01x slower                                                                                                      |
| regex_compile  | 79.4 ms                                                                                                                | 80.6 ms: 1.02x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 134 us                                                                                                                 | 119 us: 1.12x faster                                                                                                       |
| tomli_loads          | 1.33 sec                                                                                                               | 1.19 sec: 1.12x faster                                                                                                     |
| pickle_dict          | 21.0 us                                                                                                                | 19.5 us: 1.08x faster                                                                                                      |
| xml_etree_generate   | 55.3 ms                                                                                                                | 51.4 ms: 1.08x faster                                                                                                      |
| xml_etree_process    | 39.1 ms                                                                                                                | 36.9 ms: 1.06x faster                                                                                                      |
| pickle_list          | 3.59 us                                                                                                                | 3.39 us: 1.06x faster                                                                                                      |
| pickle               | 8.57 us                                                                                                                | 8.18 us: 1.05x faster                                                                                                      |
| pickle_pure_python   | 207 us                                                                                                                 | 208 us: 1.01x slower                                                                                                       |
| unpickle_list        | 2.77 us                                                                                                                | 2.78 us: 1.01x slower                                                                                                      |
| unpickle             | 8.53 us                                                                                                                | 8.70 us: 1.02x slower                                                                                                      |
| json_loads           | 14.6 us                                                                                                                | 15.2 us: 1.04x slower                                                                                                      |
| json_dumps           | 6.49 ms                                                                                                                | 6.76 ms: 1.04x slower                                                                                                      |
| xml_etree_parse      | 88.5 ms                                                                                                                | 92.1 ms: 1.04x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 26.0 ms                                                                                                                | 26.3 ms: 1.01x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.47 ms                                                                                                                | 5.67 ms: 1.14x faster                                                                                                      |
| genshi_text    | 15.1 ms                                                                                                                | 15.3 ms: 1.02x slower                                                                                                      |
| genshi_xml     | 33.1 ms                                                                                                                | 35.3 ms: 1.07x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json | results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako                     | 6.47 ms                                                                                                                | 5.67 ms: 1.14x faster                                                                                                      |
| unpickle_pure_python     | 134 us                                                                                                                 | 119 us: 1.12x faster                                                                                                       |
| tomli_loads              | 1.33 sec                                                                                                               | 1.19 sec: 1.12x faster                                                                                                     |
| nbody                    | 62.6 ms                                                                                                                | 57.0 ms: 1.10x faster                                                                                                      |
| scimark_fft              | 171 ms                                                                                                                 | 157 ms: 1.09x faster                                                                                                       |
| pickle_dict              | 21.0 us                                                                                                                | 19.5 us: 1.08x faster                                                                                                      |
| xml_etree_generate       | 55.3 ms                                                                                                                | 51.4 ms: 1.08x faster                                                                                                      |
| pyflate                  | 282 ms                                                                                                                 | 262 ms: 1.08x faster                                                                                                       |
| bpe_tokeniser            | 2.88 sec                                                                                                               | 2.70 sec: 1.07x faster                                                                                                     |
| telco                    | 4.62 ms                                                                                                                | 4.35 ms: 1.06x faster                                                                                                      |
| xml_etree_process        | 39.1 ms                                                                                                                | 36.9 ms: 1.06x faster                                                                                                      |
| pickle_list              | 3.59 us                                                                                                                | 3.39 us: 1.06x faster                                                                                                      |
| scimark_sparse_mat_mult  | 2.44 ms                                                                                                                | 2.32 ms: 1.05x faster                                                                                                      |
| fannkuch                 | 250 ms                                                                                                                 | 238 ms: 1.05x faster                                                                                                       |
| pickle                   | 8.57 us                                                                                                                | 8.18 us: 1.05x faster                                                                                                      |
| pprint_pformat           | 1.01 sec                                                                                                               | 963 ms: 1.05x faster                                                                                                       |
| k_core                   | 1.69 sec                                                                                                               | 1.62 sec: 1.04x faster                                                                                                     |
| regex_dna                | 118 ms                                                                                                                 | 116 ms: 1.02x faster                                                                                                       |
| generators               | 19.6 ms                                                                                                                | 19.2 ms: 1.02x faster                                                                                                      |
| raytrace                 | 173 ms                                                                                                                 | 171 ms: 1.02x faster                                                                                                       |
| sqlite_synth             | 1.57 us                                                                                                                | 1.55 us: 1.01x faster                                                                                                      |
| pprint_safe_repr         | 487 ms                                                                                                                 | 482 ms: 1.01x faster                                                                                                       |
| connected_components     | 324 ms                                                                                                                 | 321 ms: 1.01x faster                                                                                                       |
| mdp                      | 793 ms                                                                                                                 | 797 ms: 1.00x slower                                                                                                       |
| scimark_sor              | 73.8 ms                                                                                                                | 74.2 ms: 1.01x slower                                                                                                      |
| pickle_pure_python       | 207 us                                                                                                                 | 208 us: 1.01x slower                                                                                                       |
| unpickle_list            | 2.77 us                                                                                                                | 2.78 us: 1.01x slower                                                                                                      |
| richards                 | 27.2 ms                                                                                                                | 27.4 ms: 1.01x slower                                                                                                      |
| chaos                    | 38.7 ms                                                                                                                | 39.0 ms: 1.01x slower                                                                                                      |
| 2to3                     | 220 ms                                                                                                                 | 222 ms: 1.01x slower                                                                                                       |
| pathlib                  | 32.0 ms                                                                                                                | 32.3 ms: 1.01x slower                                                                                                      |
| meteor_contest           | 73.7 ms                                                                                                                | 74.5 ms: 1.01x slower                                                                                                      |
| subparsers               | 15.9 ms                                                                                                                | 16.1 ms: 1.01x slower                                                                                                      |
| regex_effbot             | 1.45 ms                                                                                                                | 1.47 ms: 1.01x slower                                                                                                      |
| python_startup           | 26.0 ms                                                                                                                | 26.3 ms: 1.01x slower                                                                                                      |
| sympy_sum                | 88.8 ms                                                                                                                | 89.9 ms: 1.01x slower                                                                                                      |
| deltablue                | 2.13 ms                                                                                                                | 2.16 ms: 1.01x slower                                                                                                      |
| scimark_lu               | 57.5 ms                                                                                                                | 58.3 ms: 1.01x slower                                                                                                      |
| regex_compile            | 79.4 ms                                                                                                                | 80.6 ms: 1.02x slower                                                                                                      |
| deepcopy_memo            | 18.1 us                                                                                                                | 18.4 us: 1.02x slower                                                                                                      |
| spectral_norm            | 55.5 ms                                                                                                                | 56.5 ms: 1.02x slower                                                                                                      |
| genshi_text              | 15.1 ms                                                                                                                | 15.3 ms: 1.02x slower                                                                                                      |
| dulwich_log              | 41.9 ms                                                                                                                | 42.7 ms: 1.02x slower                                                                                                      |
| html5lib                 | 38.2 ms                                                                                                                | 38.9 ms: 1.02x slower                                                                                                      |
| richards_super           | 30.9 ms                                                                                                                | 31.5 ms: 1.02x slower                                                                                                      |
| unpickle                 | 8.53 us                                                                                                                | 8.70 us: 1.02x slower                                                                                                      |
| asyncio_websockets       | 157 ms                                                                                                                 | 160 ms: 1.02x slower                                                                                                       |
| sphinx                   | 638 ms                                                                                                                 | 653 ms: 1.02x slower                                                                                                       |
| gc_traversal             | 2.04 ms                                                                                                                | 2.09 ms: 1.03x slower                                                                                                      |
| float                    | 42.2 ms                                                                                                                | 43.3 ms: 1.03x slower                                                                                                      |
| sympy_str                | 170 ms                                                                                                                 | 175 ms: 1.03x slower                                                                                                       |
| sqlglot_v2_normalize     | 70.0 ms                                                                                                                | 72.2 ms: 1.03x slower                                                                                                      |
| unpack_sequence          | 36.7 ns                                                                                                                | 37.9 ns: 1.03x slower                                                                                                      |
| deepcopy_reduce          | 1.79 us                                                                                                                | 1.85 us: 1.03x slower                                                                                                      |
| deepcopy                 | 171 us                                                                                                                 | 177 us: 1.03x slower                                                                                                       |
| pylint                   | 196 ms                                                                                                                 | 203 ms: 1.04x slower                                                                                                       |
| json_loads               | 14.6 us                                                                                                                | 15.2 us: 1.04x slower                                                                                                      |
| docutils                 | 1.64 sec                                                                                                               | 1.70 sec: 1.04x slower                                                                                                     |
| hexiom                   | 3.96 ms                                                                                                                | 4.12 ms: 1.04x slower                                                                                                      |
| json_dumps               | 6.49 ms                                                                                                                | 6.76 ms: 1.04x slower                                                                                                      |
| xml_etree_parse          | 88.5 ms                                                                                                                | 92.1 ms: 1.04x slower                                                                                                      |
| sympy_expand             | 291 ms                                                                                                                 | 305 ms: 1.05x slower                                                                                                       |
| sympy_integrate          | 12.4 ms                                                                                                                | 13.1 ms: 1.05x slower                                                                                                      |
| go                       | 76.3 ms                                                                                                                | 80.3 ms: 1.05x slower                                                                                                      |
| sqlglot_v2_optimize      | 33.6 ms                                                                                                                | 35.4 ms: 1.05x slower                                                                                                      |
| coverage                 | 48.6 ms                                                                                                                | 51.1 ms: 1.05x slower                                                                                                      |
| coroutines               | 13.5 ms                                                                                                                | 14.2 ms: 1.06x slower                                                                                                      |
| scimark_monte_carlo      | 38.2 ms                                                                                                                | 40.5 ms: 1.06x slower                                                                                                      |
| comprehensions           | 11.3 us                                                                                                                | 12.0 us: 1.06x slower                                                                                                      |
| genshi_xml               | 33.1 ms                                                                                                                | 35.3 ms: 1.07x slower                                                                                                      |
| many_optionals           | 427 us                                                                                                                 | 458 us: 1.07x slower                                                                                                       |
| typing_runtime_protocols | 104 us                                                                                                                 | 112 us: 1.08x slower                                                                                                       |
| async_generators         | 224 ms                                                                                                                 | 248 ms: 1.11x slower                                                                                                       |
| Geometric mean           | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (28): python_startup_no_site, create_gc_cycles, shortest_path, async_tree_none_tg, logging_simple, crypto_pyaes, regex_v8, sqlglot_v2_parse, async_tree_memoization_tg, logging_format, logging_silent, json, bench_mp_pool, django_template, pidigits, asyncio_tcp, nqueens, async_tree_none, sqlglot_v2_transpile, async_tree_memoization, async_tree_io_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, bench_thread_pool, async_tree_cpu_io_mixed, xml_etree_iterparse, pycparser, async_tree_io

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 97.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown