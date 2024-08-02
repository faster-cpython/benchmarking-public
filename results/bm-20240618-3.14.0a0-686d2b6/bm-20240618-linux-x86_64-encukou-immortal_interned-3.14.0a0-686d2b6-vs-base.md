# Results vs. base

- fork: encukou
- ref: immortal_interned
- machine: linux-x86_64
- commit hash: 686d2b6
- commit date: 2024-06-18
- overall geometric mean: 1.00x faster
- HPT reliability: 91.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 271 ms                                                                | 273 ms: 1.01x slower                                                |
| html5lib       | 67.3 ms                                                               | 68.3 ms: 1.01x slower                                               |
| tornado_http   | 93.8 ms                                                               | 94.2 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io  | 976 ms                                                                | 946 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                               | 86.5 ms: 1.02x faster                                               |
| float          | 78.1 ms                                                               | 77.7 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                               | 25.9 ms: 1.01x faster                                               |
| regex_compile  | 133 ms                                                                | 133 ms: 1.00x faster                                                |
| regex_effbot   | 3.76 ms                                                               | 3.83 ms: 1.02x slower                                               |
| regex_dna      | 227 ms                                                                | 235 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list        | 5.49 us                                                               | 5.18 us: 1.06x faster                                               |
| unpickle_pure_python | 219 us                                                                | 214 us: 1.02x faster                                                |
| xml_etree_parse      | 160 ms                                                                | 157 ms: 1.02x faster                                                |
| xml_etree_iterparse  | 107 ms                                                                | 106 ms: 1.01x faster                                                |
| pickle_list          | 5.05 us                                                               | 5.00 us: 1.01x faster                                               |
| json_loads           | 28.6 us                                                               | 28.3 us: 1.01x faster                                               |
| pickle               | 11.8 us                                                               | 11.9 us: 1.01x slower                                               |
| xml_etree_generate   | 85.8 ms                                                               | 87.2 ms: 1.02x slower                                               |
| xml_etree_process    | 59.8 ms                                                               | 60.9 ms: 1.02x slower                                               |
| pickle_dict          | 34.7 us                                                               | 35.6 us: 1.03x slower                                               |
| json_dumps           | 10.6 ms                                                               | 10.9 ms: 1.03x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (3): pickle_pure_python, tomli_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                               | 10.8 ms: 1.01x slower                                               |
| python_startup_no_site | 7.10 ms                                                               | 7.18 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                               | 50.4 ms: 1.02x faster                                               |
| mako            | 11.5 ms                                                               | 11.3 ms: 1.01x faster                                               |
| genshi_text     | 23.5 ms                                                               | 23.3 ms: 1.01x faster                                               |
| django_template | 34.4 ms                                                               | 34.6 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list            | 5.49 us                                                               | 5.18 us: 1.06x faster                                               |
| scimark_lu               | 118 ms                                                                | 114 ms: 1.04x faster                                                |
| json                     | 5.39 ms                                                               | 5.21 ms: 1.03x faster                                               |
| async_tree_io            | 976 ms                                                                | 946 ms: 1.03x faster                                                |
| pyflate                  | 492 ms                                                                | 478 ms: 1.03x faster                                                |
| unpickle_pure_python     | 219 us                                                                | 214 us: 1.02x faster                                                |
| bpe_tokeniser            | 5.00 sec                                                              | 4.90 sec: 1.02x faster                                              |
| nbody                    | 88.3 ms                                                               | 86.5 ms: 1.02x faster                                               |
| scimark_monte_carlo      | 69.0 ms                                                               | 67.7 ms: 1.02x faster                                               |
| genshi_xml               | 51.4 ms                                                               | 50.4 ms: 1.02x faster                                               |
| xml_etree_parse          | 160 ms                                                                | 157 ms: 1.02x faster                                                |
| xml_etree_iterparse      | 107 ms                                                                | 106 ms: 1.01x faster                                                |
| mdp                      | 2.76 sec                                                              | 2.72 sec: 1.01x faster                                              |
| regex_v8                 | 26.2 ms                                                               | 25.9 ms: 1.01x faster                                               |
| async_generators         | 446 ms                                                                | 440 ms: 1.01x faster                                                |
| comprehensions           | 17.1 us                                                               | 16.8 us: 1.01x faster                                               |
| scimark_fft              | 372 ms                                                                | 367 ms: 1.01x faster                                                |
| scimark_sor              | 135 ms                                                                | 133 ms: 1.01x faster                                                |
| typing_runtime_protocols | 164 us                                                                | 162 us: 1.01x faster                                                |
| mako                     | 11.5 ms                                                               | 11.3 ms: 1.01x faster                                               |
| pathlib                  | 16.3 ms                                                               | 16.2 ms: 1.01x faster                                               |
| genshi_text              | 23.5 ms                                                               | 23.3 ms: 1.01x faster                                               |
| pickle_list              | 5.05 us                                                               | 5.00 us: 1.01x faster                                               |
| pprint_pformat           | 1.55 sec                                                              | 1.53 sec: 1.01x faster                                              |
| pprint_safe_repr         | 752 ms                                                                | 745 ms: 1.01x faster                                                |
| json_loads               | 28.6 us                                                               | 28.3 us: 1.01x faster                                               |
| telco                    | 8.40 ms                                                               | 8.32 ms: 1.01x faster                                               |
| sympy_sum                | 156 ms                                                                | 154 ms: 1.01x faster                                                |
| sqlglot_normalize        | 110 ms                                                                | 109 ms: 1.01x faster                                                |
| sqlglot_parse            | 1.33 ms                                                               | 1.32 ms: 1.01x faster                                               |
| float                    | 78.1 ms                                                               | 77.7 ms: 1.01x faster                                               |
| sqlglot_optimize         | 54.8 ms                                                               | 54.6 ms: 1.00x faster                                               |
| dulwich_log              | 65.5 ms                                                               | 65.2 ms: 1.00x faster                                               |
| regex_compile            | 133 ms                                                                | 133 ms: 1.00x faster                                                |
| sympy_integrate          | 20.3 ms                                                               | 20.3 ms: 1.00x faster                                               |
| bench_thread_pool        | 834 us                                                                | 832 us: 1.00x faster                                                |
| asyncio_tcp_ssl          | 1.83 sec                                                              | 1.83 sec: 1.00x slower                                              |
| hexiom                   | 6.16 ms                                                               | 6.18 ms: 1.00x slower                                               |
| coverage                 | 93.4 ms                                                               | 93.8 ms: 1.00x slower                                               |
| create_gc_cycles         | 1.74 ms                                                               | 1.75 ms: 1.00x slower                                               |
| deepcopy                 | 266 us                                                                | 267 us: 1.00x slower                                                |
| tornado_http             | 93.8 ms                                                               | 94.2 ms: 1.00x slower                                               |
| django_template          | 34.4 ms                                                               | 34.6 ms: 1.01x slower                                               |
| richards_super           | 55.1 ms                                                               | 55.5 ms: 1.01x slower                                               |
| 2to3                     | 271 ms                                                                | 273 ms: 1.01x slower                                                |
| generators               | 29.2 ms                                                               | 29.5 ms: 1.01x slower                                               |
| meteor_contest           | 109 ms                                                                | 109 ms: 1.01x slower                                                |
| pickle                   | 11.8 us                                                               | 11.9 us: 1.01x slower                                               |
| python_startup           | 10.7 ms                                                               | 10.8 ms: 1.01x slower                                               |
| deepcopy_reduce          | 2.69 us                                                               | 2.72 us: 1.01x slower                                               |
| thrift                   | 796 us                                                                | 804 us: 1.01x slower                                                |
| nqueens                  | 79.5 ms                                                               | 80.3 ms: 1.01x slower                                               |
| python_startup_no_site   | 7.10 ms                                                               | 7.18 ms: 1.01x slower                                               |
| html5lib                 | 67.3 ms                                                               | 68.3 ms: 1.01x slower                                               |
| xml_etree_generate       | 85.8 ms                                                               | 87.2 ms: 1.02x slower                                               |
| logging_silent           | 103 ns                                                                | 104 ns: 1.02x slower                                                |
| coroutines               | 22.6 ms                                                               | 23.0 ms: 1.02x slower                                               |
| asyncio_tcp              | 488 ms                                                                | 497 ms: 1.02x slower                                                |
| xml_etree_process        | 59.8 ms                                                               | 60.9 ms: 1.02x slower                                               |
| regex_effbot             | 3.76 ms                                                               | 3.83 ms: 1.02x slower                                               |
| logging_simple           | 5.67 us                                                               | 5.82 us: 1.03x slower                                               |
| pickle_dict              | 34.7 us                                                               | 35.6 us: 1.03x slower                                               |
| json_dumps               | 10.6 ms                                                               | 10.9 ms: 1.03x slower                                               |
| logging_format           | 6.31 us                                                               | 6.49 us: 1.03x slower                                               |
| regex_dna                | 227 ms                                                                | 235 ms: 1.03x slower                                                |
| gc_traversal             | 3.57 ms                                                               | 3.81 ms: 1.07x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (31): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, pycparser, go, fannkuch, async_tree_none, sqlite_synth, dask, sqlglot_transpile, richards, deepcopy_memo, pylint, pidigits, asyncio_websockets, sympy_str, bench_mp_pool, raytrace, sympy_expand, pickle_pure_python, docutils, scimark_sparse_mat_mult, deltablue, spectral_norm, tomli_loads, crypto_pyaes, chaos, async_tree_io_tg, unpickle

# HPT report

- Reliability score: 91.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x