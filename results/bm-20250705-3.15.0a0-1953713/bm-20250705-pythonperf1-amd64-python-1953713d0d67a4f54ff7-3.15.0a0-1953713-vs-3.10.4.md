# Results vs. 3.10.4

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.277x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 393 ms: 2.82x faster                                                       |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.57x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.95x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 64.3 ms: 1.11x faster                                                      |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.2 ms: 1.32x faster                                                      |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.41 ms: 1.43x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.26x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.41 sec: 1.19x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.47 us: 1.07x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.76 us: 1.02x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.5 us: 1.14x slower                                                      |
| pickle               | 6.85 us                                                     | 7.99 us: 1.17x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.33 us: 1.21x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.85 ms: 1.32x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| django_template | 28.9 ms                                                     | 23.7 ms: 1.22x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 33.8 ms: 1.21x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 393 ms: 2.82x faster                                                       |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.57x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.6 ms: 2.39x faster                                                      |
| mdp                      | 1.78 sec                                                    | 817 ms: 2.18x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                      |
| go                       | 139 ms                                                      | 77.7 ms: 1.79x faster                                                      |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.5 ns: 1.71x faster                                                      |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.70x faster                                                      |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 449 ms: 1.63x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.33 sec: 1.58x faster                                                     |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.5 us: 1.56x faster                                                      |
| raytrace                 | 273 ms                                                      | 178 ms: 1.54x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.7 ms: 1.52x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.52x faster                                                      |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 57.8 ms: 1.48x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.41 ms: 1.43x faster                                                      |
| float                    | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.8 ms: 1.40x faster                                                      |
| pyflate                  | 409 ms                                                      | 292 ms: 1.40x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.16 ms: 1.38x faster                                                      |
| scimark_sor              | 106 ms                                                      | 77.4 ms: 1.37x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                       |
| regex_compile            | 106 ms                                                      | 80.2 ms: 1.32x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.85 ms: 1.32x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                      |
| pycparser                | 930 ms                                                      | 714 ms: 1.30x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.2 ms: 1.30x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.26x faster                                                       |
| thrift                   | 617 us                                                      | 493 us: 1.25x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.6 ms: 1.24x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.2 ms: 1.23x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.7 ms: 1.22x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 33.8 ms: 1.21x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 63.9 ms: 1.21x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 493 ms: 1.20x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                     |
| tomli_loads              | 1.67 sec                                                    | 1.41 sec: 1.19x faster                                                     |
| sympy_str                | 194 ms                                                      | 168 ms: 1.15x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 847 us: 1.13x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                      |
| nbody                    | 71.3 ms                                                     | 64.3 ms: 1.11x faster                                                      |
| sympy_expand             | 314 ms                                                      | 286 ms: 1.10x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.49 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 36.5 ns: 1.09x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 61.5 ms: 1.08x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.47 us: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.5 ms: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                      |
| scimark_fft              | 187 ms                                                      | 180 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.2 ms: 1.04x faster                                                      |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.26 us: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.76 us: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                       |
| fannkuch                 | 256 ms                                                      | 270 ms: 1.06x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.5 us: 1.14x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.54 ms: 1.15x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.99 us: 1.17x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.33 us: 1.21x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.7 ms: 1.30x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 95.2 ms: 1.53x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.64x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                               |

Benchmark hidden because not significant (2): logging_format, xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250705-3.15.0a0-1953713/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.277x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown