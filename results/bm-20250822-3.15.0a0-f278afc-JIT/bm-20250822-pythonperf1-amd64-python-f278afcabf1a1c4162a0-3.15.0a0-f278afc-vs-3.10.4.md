# Results vs. 3.10.4

- fork: python
- ref: f278afcabf1a1c4162a0
- machine: windows-amd64
- commit hash: f278afc
- commit date: 2025-08-22
- overall geometric mean: 1.351x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 214 ms: 1.15x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 378 ms: 2.93x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 199 ms: 2.65x faster                                                       |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.49x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.6 ms: 1.45x faster                                                      |
| nbody          | 71.3 ms                                                     | 53.6 ms: 1.33x faster                                                      |
| pidigits       | 149 ms                                                      | 144 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.0 ms: 1.38x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 104 us: 1.76x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.42 ms: 1.69x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.08 sec: 1.54x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 198 us: 1.36x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 34.6 ms: 1.29x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 84.2 ms: 1.15x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 49.2 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.0 ms: 1.07x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.30x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.36 ms: 1.68x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 98.7 us: 3.40x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 378 ms: 2.93x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 199 ms: 2.65x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.6 ms: 2.55x faster                                                      |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                       |
| mdp                      | 1.78 sec                                                    | 775 ms: 2.30x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                      |
| go                       | 139 ms                                                      | 74.8 ms: 1.86x faster                                                      |
| pylint                   | 350 ms                                                      | 194 ms: 1.81x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 104 us: 1.76x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 53.7 ns: 1.76x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.3 ms: 1.72x faster                                                      |
| generators               | 32.4 ms                                                     | 19.0 ms: 1.70x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.42 ms: 1.69x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.36 ms: 1.68x faster                                                      |
| raytrace                 | 273 ms                                                      | 168 ms: 1.63x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.60x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.6 ms: 1.59x faster                                                      |
| pyflate                  | 409 ms                                                      | 263 ms: 1.56x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.9 ms: 1.55x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.08 sec: 1.54x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 19.0 us: 1.51x faster                                                      |
| deepcopy                 | 255 us                                                      | 172 us: 1.49x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.1 ms: 1.48x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 3.94 ms: 1.46x faster                                                      |
| float                    | 61.7 ms                                                     | 42.6 ms: 1.45x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.7 ms: 1.44x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 847 ms: 1.44x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 419 ms: 1.41x faster                                                       |
| scimark_sor              | 106 ms                                                      | 75.5 ms: 1.41x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 44.7 ms: 1.40x faster                                                      |
| regex_compile            | 106 ms                                                      | 77.0 ms: 1.38x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 198 us: 1.36x faster                                                       |
| pycparser                | 930 ms                                                      | 690 ms: 1.35x faster                                                       |
| nbody                    | 71.3 ms                                                     | 53.6 ms: 1.33x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.5 ms: 1.33x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 39.0 ms: 1.29x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 34.6 ms: 1.29x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.27x faster                                                      |
| thrift                   | 617 us                                                      | 486 us: 1.27x faster                                                       |
| fannkuch                 | 256 ms                                                      | 204 ms: 1.26x faster                                                       |
| sympy_sum                | 107 ms                                                      | 85.3 ms: 1.25x faster                                                      |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 62.9 ms: 1.23x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.31 ms: 1.18x faster                                                      |
| sympy_str                | 194 ms                                                      | 167 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 84.2 ms: 1.15x faster                                                      |
| 2to3                     | 246 ms                                                      | 214 ms: 1.15x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 58.8 ms: 1.13x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.2 ms: 1.13x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.7 ms: 1.13x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 69.3 ms: 1.10x faster                                                      |
| sympy_expand             | 314 ms                                                      | 289 ms: 1.09x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.0 ms: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.41 us: 1.06x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.92 us: 1.05x faster                                                      |
| telco                    | 3.94 ms                                                     | 3.79 ms: 1.04x faster                                                      |
| json                     | 3.14 ms                                                     | 3.03 ms: 1.04x faster                                                      |
| pidigits                 | 149 ms                                                      | 144 ms: 1.03x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 241 ms: 1.09x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                      |
| coverage                 | 39.0 ms                                                     | 48.9 ms: 1.25x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.47x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.30 ms: 1.62x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.35x faster                                                               |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250822-3.15.0a0-f278afc-JIT/bm-20250822-pythonperf1-amd64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.351x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: unknown