# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-amd64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 243 ms: 1.01x faster                                                         |
| html5lib       | 51.0 ms                                                     | 41.8 ms: 1.22x faster                                                        |
| tornado_http   | 108 ms                                                      | 97.2 ms: 1.11x faster                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 203 ms: 2.14x faster                                                         |
| async_tree_memoization  | 526 ms                                                      | 257 ms: 2.05x faster                                                         |
| async_tree_io           | 1.11 sec                                                    | 580 ms: 1.91x faster                                                         |
| async_tree_cpu_io_mixed | 638 ms                                                      | 392 ms: 1.62x faster                                                         |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.8 ms: 1.43x faster                                                        |
| float          | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                        |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                         |
| regex_compile  | 106 ms                                                      | 95.1 ms: 1.12x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.91 ms: 1.55x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 197 us: 1.37x faster                                                         |
| tomli_loads          | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 142 us: 1.29x faster                                                         |
| xml_etree_process    | 44.5 ms                                                     | 35.0 ms: 1.27x faster                                                        |
| xml_etree_generate   | 55.5 ms                                                     | 49.7 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                        |
| xml_etree_parse      | 96.8 ms                                                     | 94.1 ms: 1.03x faster                                                        |
| pickle_list          | 2.75 us                                                     | 2.82 us: 1.02x slower                                                        |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                        |
| pickle_dict          | 17.2 us                                                     | 17.7 us: 1.03x slower                                                        |
| unpickle_list        | 2.71 us                                                     | 2.86 us: 1.05x slower                                                        |
| pickle               | 6.85 us                                                     | 7.25 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.6 ms: 1.10x slower                                                        |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.00 ms: 1.81x faster                                                        |
| django_template | 28.9 ms                                                     | 26.6 ms: 1.09x faster                                                        |
| genshi_text     | 19.8 ms                                                     | 19.3 ms: 1.03x faster                                                        |
| genshi_xml      | 41.0 ms                                                     | 46.0 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.10x faster                                                         |
| deltablue                | 4.19 ms                                                     | 1.84 ms: 2.27x faster                                                        |
| async_tree_none          | 435 ms                                                      | 203 ms: 2.14x faster                                                         |
| async_tree_memoization   | 526 ms                                                      | 257 ms: 2.05x faster                                                         |
| async_tree_io            | 1.11 sec                                                    | 580 ms: 1.91x faster                                                         |
| deepcopy_memo            | 28.8 us                                                     | 15.7 us: 1.83x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.00 ms: 1.81x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 44.0 ms: 1.75x faster                                                        |
| scimark_sor              | 106 ms                                                      | 60.5 ms: 1.75x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 57.9 ns: 1.63x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 392 ms: 1.62x faster                                                         |
| crypto_pyaes             | 62.5 ms                                                     | 38.8 ms: 1.61x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 54.3 ms: 1.58x faster                                                        |
| pyflate                  | 409 ms                                                      | 261 ms: 1.57x faster                                                         |
| json_dumps               | 9.16 ms                                                     | 5.91 ms: 1.55x faster                                                        |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                        |
| chaos                    | 61.7 ms                                                     | 40.6 ms: 1.52x faster                                                        |
| go                       | 139 ms                                                      | 92.7 ms: 1.50x faster                                                        |
| generators               | 32.4 ms                                                     | 22.5 ms: 1.44x faster                                                        |
| nbody                    | 71.3 ms                                                     | 49.8 ms: 1.43x faster                                                        |
| float                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                        |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                         |
| pickle_pure_python       | 270 us                                                      | 197 us: 1.37x faster                                                         |
| sqlglot_parse            | 1.22 ms                                                     | 898 us: 1.35x faster                                                         |
| tomli_loads              | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.0 ms: 1.33x faster                                                        |
| pylint                   | 350 ms                                                      | 265 ms: 1.32x faster                                                         |
| richards_super           | 52.2 ms                                                     | 39.8 ms: 1.31x faster                                                        |
| raytrace                 | 273 ms                                                      | 209 ms: 1.31x faster                                                         |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.62 sec: 1.30x faster                                                       |
| pycparser                | 930 ms                                                      | 716 ms: 1.30x faster                                                         |
| unpickle_pure_python     | 183 us                                                      | 142 us: 1.29x faster                                                         |
| sqlglot_transpile        | 1.48 ms                                                     | 1.16 ms: 1.27x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 35.0 ms: 1.27x faster                                                        |
| scimark_fft              | 187 ms                                                      | 149 ms: 1.26x faster                                                         |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.17 ms: 1.25x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 41.8 ms: 1.22x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                       |
| thrift                   | 617 us                                                      | 510 us: 1.21x faster                                                         |
| asyncio_tcp              | 732 ms                                                      | 611 ms: 1.20x faster                                                         |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.18x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 812 us: 1.18x faster                                                         |
| hexiom                   | 5.74 ms                                                     | 4.90 ms: 1.17x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                                        |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                        |
| richards                 | 42.4 ms                                                     | 37.3 ms: 1.14x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 523 ms: 1.13x faster                                                         |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                         |
| xml_etree_generate       | 55.5 ms                                                     | 49.7 ms: 1.12x faster                                                        |
| regex_compile            | 106 ms                                                      | 95.1 ms: 1.12x faster                                                        |
| tornado_http             | 108 ms                                                      | 97.2 ms: 1.11x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 60.8 ms: 1.10x faster                                                        |
| sympy_sum                | 107 ms                                                      | 98.3 ms: 1.09x faster                                                        |
| django_template          | 28.9 ms                                                     | 26.6 ms: 1.09x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.39 us: 1.06x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                        |
| json                     | 3.14 ms                                                     | 2.99 ms: 1.05x faster                                                        |
| logging_simple           | 6.22 us                                                     | 5.96 us: 1.04x faster                                                        |
| fannkuch                 | 256 ms                                                      | 247 ms: 1.04x faster                                                         |
| sympy_str                | 194 ms                                                      | 188 ms: 1.03x faster                                                         |
| sympy_integrate          | 15.3 ms                                                     | 14.8 ms: 1.03x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 94.1 ms: 1.03x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 19.3 ms: 1.03x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 201 ms: 1.02x faster                                                         |
| meteor_contest           | 75.9 ms                                                     | 75.1 ms: 1.01x faster                                                        |
| 2to3                     | 246 ms                                                      | 243 ms: 1.01x faster                                                         |
| sqlglot_optimize         | 39.8 ms                                                     | 40.4 ms: 1.02x slower                                                        |
| pickle_list              | 2.75 us                                                     | 2.82 us: 1.02x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                        |
| pickle_dict              | 17.2 us                                                     | 17.7 us: 1.03x slower                                                        |
| sympy_expand             | 314 ms                                                      | 329 ms: 1.05x slower                                                         |
| pathlib                  | 75.7 ms                                                     | 79.6 ms: 1.05x slower                                                        |
| unpickle_list            | 2.71 us                                                     | 2.86 us: 1.05x slower                                                        |
| pickle                   | 6.85 us                                                     | 7.25 us: 1.06x slower                                                        |
| gc_traversal             | 1.41 ms                                                     | 1.54 ms: 1.09x slower                                                        |
| python_startup           | 20.6 ms                                                     | 22.6 ms: 1.10x slower                                                        |
| create_gc_cycles         | 800 us                                                      | 896 us: 1.12x slower                                                         |
| genshi_xml               | 41.0 ms                                                     | 46.0 ms: 1.12x slower                                                        |
| async_generators         | 222 ms                                                      | 257 ms: 1.16x slower                                                         |
| telco                    | 3.94 ms                                                     | 4.57 ms: 1.16x slower                                                        |
| bench_mp_pool            | 62.0 ms                                                     | 72.1 ms: 1.16x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                        |
| coverage                 | 39.0 ms                                                     | 47.7 ms: 1.22x slower                                                        |
| unpack_sequence          | 39.6 ns                                                     | 58.8 ns: 1.48x slower                                                        |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                 |

Benchmark hidden because not significant (4): unpickle, docutils, pidigits, regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown