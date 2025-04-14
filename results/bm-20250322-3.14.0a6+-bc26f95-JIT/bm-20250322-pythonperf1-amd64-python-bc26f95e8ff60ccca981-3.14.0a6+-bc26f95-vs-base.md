# Results vs. base

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-amd64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.016x faster
- HPT reliability: 95.27%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 226 ms                                                                                                                 | 229 ms: 1.01x slower                                                                                                       |
| docutils       | 1.69 sec                                                                                                               | 1.75 sec: 1.04x slower                                                                                                     |
| sphinx         | 660 ms                                                                                                                 | 671 ms: 1.02x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|-------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io           | 430 ms                                                                                                                 | 417 ms: 1.03x faster                                                                                                       |
| async_tree_io_tg        | 417 ms                                                                                                                 | 412 ms: 1.01x faster                                                                                                       |
| async_tree_cpu_io_mixed | 338 ms                                                                                                                 | 336 ms: 1.01x faster                                                                                                       |
| coroutines              | 13.7 ms                                                                                                                | 13.9 ms: 1.02x slower                                                                                                      |
| async_generators        | 230 ms                                                                                                                 | 249 ms: 1.08x slower                                                                                                       |
| Geometric mean          | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (8): asyncio_websockets, asyncio_tcp, async_tree_none, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 67.3 ms                                                                                                                | 59.7 ms: 1.13x faster                                                                                                      |
| pidigits       | 148 ms                                                                                                                 | 149 ms: 1.00x slower                                                                                                       |
| float          | 46.4 ms                                                                                                                | 48.3 ms: 1.04x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 87.3 ms                                                                                                                | 86.5 ms: 1.01x faster                                                                                                      |
| regex_v8       | 14.0 ms                                                                                                                | 13.8 ms: 1.01x faster                                                                                                      |
| regex_dna      | 117 ms                                                                                                                 | 118 ms: 1.01x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.51 sec                                                                                                               | 1.23 sec: 1.22x faster                                                                                                     |
| unpickle_pure_python | 150 us                                                                                                                 | 123 us: 1.22x faster                                                                                                       |
| xml_etree_process    | 42.1 ms                                                                                                                | 38.3 ms: 1.10x faster                                                                                                      |
| xml_etree_generate   | 58.6 ms                                                                                                                | 54.2 ms: 1.08x faster                                                                                                      |
| pickle_dict          | 20.8 us                                                                                                                | 19.8 us: 1.05x faster                                                                                                      |
| pickle_pure_python   | 227 us                                                                                                                 | 217 us: 1.04x faster                                                                                                       |
| pickle_list          | 3.52 us                                                                                                                | 3.38 us: 1.04x faster                                                                                                      |
| xml_etree_iterparse  | 64.0 ms                                                                                                                | 62.4 ms: 1.03x faster                                                                                                      |
| xml_etree_parse      | 89.7 ms                                                                                                                | 89.0 ms: 1.01x faster                                                                                                      |
| json_loads           | 15.0 us                                                                                                                | 15.1 us: 1.01x slower                                                                                                      |
| json_dumps           | 6.92 ms                                                                                                                | 7.04 ms: 1.02x slower                                                                                                      |
| unpickle             | 8.42 us                                                                                                                | 8.60 us: 1.02x slower                                                                                                      |
| pickle               | 8.11 us                                                                                                                | 8.49 us: 1.05x slower                                                                                                      |
| unpickle_list        | 2.75 us                                                                                                                | 2.89 us: 1.05x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 25.9 ms                                                                                                                | 25.7 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako           | 6.84 ms                                                                                                                | 5.88 ms: 1.16x faster                                                                                                      |
| genshi_text    | 17.1 ms                                                                                                                | 17.4 ms: 1.02x slower                                                                                                      |
| genshi_xml     | 38.4 ms                                                                                                                | 40.8 ms: 1.06x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.02x faster                                                                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json | results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json |
|--------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads              | 1.51 sec                                                                                                               | 1.23 sec: 1.22x faster                                                                                                     |
| unpickle_pure_python     | 150 us                                                                                                                 | 123 us: 1.22x faster                                                                                                       |
| mako                     | 6.84 ms                                                                                                                | 5.88 ms: 1.16x faster                                                                                                      |
| scimark_sparse_mat_mult  | 2.62 ms                                                                                                                | 2.27 ms: 1.16x faster                                                                                                      |
| pyflate                  | 318 ms                                                                                                                 | 276 ms: 1.15x faster                                                                                                       |
| scimark_fft              | 181 ms                                                                                                                 | 158 ms: 1.14x faster                                                                                                       |
| nbody                    | 67.3 ms                                                                                                                | 59.7 ms: 1.13x faster                                                                                                      |
| fannkuch                 | 282 ms                                                                                                                 | 253 ms: 1.12x faster                                                                                                       |
| xml_etree_process        | 42.1 ms                                                                                                                | 38.3 ms: 1.10x faster                                                                                                      |
| bpe_tokeniser            | 3.04 sec                                                                                                               | 2.79 sec: 1.09x faster                                                                                                     |
| xml_etree_generate       | 58.6 ms                                                                                                                | 54.2 ms: 1.08x faster                                                                                                      |
| pprint_safe_repr         | 554 ms                                                                                                                 | 520 ms: 1.06x faster                                                                                                       |
| pprint_pformat           | 1.11 sec                                                                                                               | 1.04 sec: 1.06x faster                                                                                                     |
| pickle_dict              | 20.8 us                                                                                                                | 19.8 us: 1.05x faster                                                                                                      |
| pickle_pure_python       | 227 us                                                                                                                 | 217 us: 1.04x faster                                                                                                       |
| mdp                      | 1.57 sec                                                                                                               | 1.50 sec: 1.04x faster                                                                                                     |
| k_core                   | 1.73 sec                                                                                                               | 1.66 sec: 1.04x faster                                                                                                     |
| telco                    | 4.82 ms                                                                                                                | 4.63 ms: 1.04x faster                                                                                                      |
| pickle_list              | 3.52 us                                                                                                                | 3.38 us: 1.04x faster                                                                                                      |
| nqueens                  | 64.5 ms                                                                                                                | 62.3 ms: 1.04x faster                                                                                                      |
| unpack_sequence          | 37.7 ns                                                                                                                | 36.4 ns: 1.03x faster                                                                                                      |
| richards_super           | 35.0 ms                                                                                                                | 33.9 ms: 1.03x faster                                                                                                      |
| async_tree_io            | 430 ms                                                                                                                 | 417 ms: 1.03x faster                                                                                                       |
| connected_components     | 335 ms                                                                                                                 | 325 ms: 1.03x faster                                                                                                       |
| richards                 | 30.7 ms                                                                                                                | 29.8 ms: 1.03x faster                                                                                                      |
| comprehensions           | 12.2 us                                                                                                                | 11.9 us: 1.03x faster                                                                                                      |
| xml_etree_iterparse      | 64.0 ms                                                                                                                | 62.4 ms: 1.03x faster                                                                                                      |
| meteor_contest           | 78.3 ms                                                                                                                | 76.3 ms: 1.03x faster                                                                                                      |
| shortest_path            | 370 ms                                                                                                                 | 362 ms: 1.02x faster                                                                                                       |
| scimark_sor              | 82.4 ms                                                                                                                | 80.6 ms: 1.02x faster                                                                                                      |
| sqlite_synth             | 1.57 us                                                                                                                | 1.54 us: 1.02x faster                                                                                                      |
| gc_traversal             | 2.08 ms                                                                                                                | 2.04 ms: 1.02x faster                                                                                                      |
| crypto_pyaes             | 50.3 ms                                                                                                                | 49.5 ms: 1.02x faster                                                                                                      |
| logging_simple           | 6.71 us                                                                                                                | 6.61 us: 1.02x faster                                                                                                      |
| async_tree_io_tg         | 417 ms                                                                                                                 | 412 ms: 1.01x faster                                                                                                       |
| scimark_lu               | 61.2 ms                                                                                                                | 60.5 ms: 1.01x faster                                                                                                      |
| scimark_monte_carlo      | 44.4 ms                                                                                                                | 43.9 ms: 1.01x faster                                                                                                      |
| regex_compile            | 87.3 ms                                                                                                                | 86.5 ms: 1.01x faster                                                                                                      |
| regex_v8                 | 14.0 ms                                                                                                                | 13.8 ms: 1.01x faster                                                                                                      |
| python_startup           | 25.9 ms                                                                                                                | 25.7 ms: 1.01x faster                                                                                                      |
| create_gc_cycles         | 1.25 ms                                                                                                                | 1.24 ms: 1.01x faster                                                                                                      |
| go                       | 89.9 ms                                                                                                                | 89.2 ms: 1.01x faster                                                                                                      |
| async_tree_cpu_io_mixed  | 338 ms                                                                                                                 | 336 ms: 1.01x faster                                                                                                       |
| xml_etree_parse          | 89.7 ms                                                                                                                | 89.0 ms: 1.01x faster                                                                                                      |
| pidigits                 | 148 ms                                                                                                                 | 149 ms: 1.00x slower                                                                                                       |
| json_loads               | 15.0 us                                                                                                                | 15.1 us: 1.01x slower                                                                                                      |
| regex_dna                | 117 ms                                                                                                                 | 118 ms: 1.01x slower                                                                                                       |
| sqlglot_v2_parse         | 916 us                                                                                                                 | 925 us: 1.01x slower                                                                                                       |
| 2to3                     | 226 ms                                                                                                                 | 229 ms: 1.01x slower                                                                                                       |
| coverage                 | 49.8 ms                                                                                                                | 50.4 ms: 1.01x slower                                                                                                      |
| pathlib                  | 32.7 ms                                                                                                                | 33.1 ms: 1.01x slower                                                                                                      |
| sympy_sum                | 90.7 ms                                                                                                                | 91.8 ms: 1.01x slower                                                                                                      |
| deepcopy                 | 186 us                                                                                                                 | 188 us: 1.01x slower                                                                                                       |
| spectral_norm            | 59.3 ms                                                                                                                | 60.2 ms: 1.02x slower                                                                                                      |
| json                     | 3.03 ms                                                                                                                | 3.08 ms: 1.02x slower                                                                                                      |
| sphinx                   | 660 ms                                                                                                                 | 671 ms: 1.02x slower                                                                                                       |
| json_dumps               | 6.92 ms                                                                                                                | 7.04 ms: 1.02x slower                                                                                                      |
| genshi_text              | 17.1 ms                                                                                                                | 17.4 ms: 1.02x slower                                                                                                      |
| coroutines               | 13.7 ms                                                                                                                | 13.9 ms: 1.02x slower                                                                                                      |
| unpickle                 | 8.42 us                                                                                                                | 8.60 us: 1.02x slower                                                                                                      |
| generators               | 19.7 ms                                                                                                                | 20.1 ms: 1.02x slower                                                                                                      |
| logging_silent           | 60.4 ns                                                                                                                | 61.8 ns: 1.02x slower                                                                                                      |
| sqlglot_v2_optimize      | 36.6 ms                                                                                                                | 37.4 ms: 1.02x slower                                                                                                      |
| sympy_integrate          | 13.2 ms                                                                                                                | 13.5 ms: 1.02x slower                                                                                                      |
| sympy_str                | 178 ms                                                                                                                 | 182 ms: 1.02x slower                                                                                                       |
| sqlglot_v2_transpile     | 1.12 ms                                                                                                                | 1.15 ms: 1.03x slower                                                                                                      |
| chaos                    | 42.3 ms                                                                                                                | 43.8 ms: 1.04x slower                                                                                                      |
| dulwich_log              | 42.4 ms                                                                                                                | 43.9 ms: 1.04x slower                                                                                                      |
| docutils                 | 1.69 sec                                                                                                               | 1.75 sec: 1.04x slower                                                                                                     |
| deepcopy_reduce          | 1.96 us                                                                                                                | 2.04 us: 1.04x slower                                                                                                      |
| float                    | 46.4 ms                                                                                                                | 48.3 ms: 1.04x slower                                                                                                      |
| sympy_expand             | 309 ms                                                                                                                 | 322 ms: 1.04x slower                                                                                                       |
| typing_runtime_protocols | 110 us                                                                                                                 | 115 us: 1.04x slower                                                                                                       |
| pickle                   | 8.11 us                                                                                                                | 8.49 us: 1.05x slower                                                                                                      |
| unpickle_list            | 2.75 us                                                                                                                | 2.89 us: 1.05x slower                                                                                                      |
| deltablue                | 2.30 ms                                                                                                                | 2.41 ms: 1.05x slower                                                                                                      |
| many_optionals           | 440 us                                                                                                                 | 463 us: 1.05x slower                                                                                                       |
| genshi_xml               | 38.4 ms                                                                                                                | 40.8 ms: 1.06x slower                                                                                                      |
| async_generators         | 230 ms                                                                                                                 | 249 ms: 1.08x slower                                                                                                       |
| hexiom                   | 4.44 ms                                                                                                                | 4.82 ms: 1.08x slower                                                                                                      |
| Geometric mean           | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (22): asyncio_websockets, asyncio_tcp, django_template, async_tree_none, logging_format, asyncio_tcp_ssl, python_startup_no_site, async_tree_memoization_tg, subparsers, raytrace, sqlglot_v2_normalize, bench_mp_pool, async_tree_cpu_io_mixed_tg, deepcopy_memo, pycparser, async_tree_none_tg, thrift, regex_effbot, bench_thread_pool, async_tree_memoization, html5lib, pylint

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 95.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown