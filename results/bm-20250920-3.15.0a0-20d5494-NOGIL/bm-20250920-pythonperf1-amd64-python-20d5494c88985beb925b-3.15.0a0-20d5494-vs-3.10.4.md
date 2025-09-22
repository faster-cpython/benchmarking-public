# Results vs. 3.10.4

- fork: python
- ref: 20d5494c88985beb925b
- machine: windows-amd64
- commit hash: 20d5494
- commit date: 2025-09-20
- overall geometric mean: 1.166x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.74 sec: 1.43x slower                                                     |
| html5lib       | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 347 ms: 3.20x faster                                                       |
| async_tree_none         | 435 ms                                                      | 167 ms: 2.60x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.53x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 325 ms: 1.96x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.54x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.2 ms: 1.33x faster                                                      |
| pidigits       | 149 ms                                                      | 136 ms: 1.09x faster                                                       |
| nbody          | 71.3 ms                                                     | 85.1 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 112 ms: 1.22x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                      |
| regex_compile  | 106 ms                                                      | 92.1 ms: 1.15x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 156 us: 1.18x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 233 us: 1.16x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 58.8 ms: 1.10x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.1 ms: 1.10x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 44.0 ms: 1.01x faster                                                      |
| pickle_list          | 2.75 us                                                     | 3.00 us: 1.09x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.1 us: 1.11x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.03 us: 1.12x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 62.3 ms: 1.12x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.0 us: 1.14x slower                                                      |
| pickle               | 6.85 us                                                     | 8.17 us: 1.19x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 21.6 us: 1.26x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.31 sec: 1.38x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 40.1 ms: 1.02x faster                                                      |
| mako            | 9.03 ms                                                     | 9.82 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 347 ms: 3.20x faster                                                       |
| async_tree_none          | 435 ms                                                      | 167 ms: 2.60x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 130 us: 2.59x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 29.6 ms: 2.56x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.53x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 325 ms: 1.96x faster                                                       |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.47 ms: 1.70x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.10 sec: 1.63x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 18.8 us: 1.53x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 61.8 ns: 1.53x faster                                                      |
| go                       | 139 ms                                                      | 91.3 ms: 1.52x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.36 us: 1.41x faster                                                      |
| generators               | 32.4 ms                                                     | 23.4 ms: 1.39x faster                                                      |
| deepcopy                 | 255 us                                                      | 187 us: 1.36x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 540 ms: 1.36x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.35x faster                                                      |
| richards_super           | 52.2 ms                                                     | 38.9 ms: 1.34x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 64.1 ms: 1.34x faster                                                      |
| float                    | 61.7 ms                                                     | 46.2 ms: 1.33x faster                                                      |
| chaos                    | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                      |
| pyflate                  | 409 ms                                                      | 311 ms: 1.32x faster                                                       |
| raytrace                 | 273 ms                                                      | 212 ms: 1.29x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                      |
| pycparser                | 930 ms                                                      | 722 ms: 1.29x faster                                                       |
| richards                 | 42.4 ms                                                     | 33.2 ms: 1.28x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.61 ms: 1.24x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.14 ms: 1.24x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                      |
| regex_dna                | 136 ms                                                      | 112 ms: 1.22x faster                                                       |
| scimark_sor              | 106 ms                                                      | 89.5 ms: 1.19x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 156 us: 1.18x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 233 us: 1.16x faster                                                       |
| regex_compile            | 106 ms                                                      | 92.1 ms: 1.15x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 50.0 ms: 1.15x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                      |
| sympy_sum                | 107 ms                                                      | 96.3 ms: 1.11x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 58.8 ms: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                       |
| thrift                   | 617 us                                                      | 561 us: 1.10x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 56.9 ms: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.1 ms: 1.10x faster                                                      |
| pidigits                 | 149 ms                                                      | 136 ms: 1.09x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 37.0 ns: 1.07x faster                                                      |
| django_template          | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.09 us: 1.06x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 73.6 ms: 1.05x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 567 ms: 1.04x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                      |
| sympy_str                | 194 ms                                                      | 188 ms: 1.03x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 40.1 ms: 1.02x faster                                                      |
| json                     | 3.14 ms                                                     | 3.09 ms: 1.01x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 44.0 ms: 1.01x faster                                                      |
| sympy_expand             | 314 ms                                                      | 320 ms: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.58 us: 1.06x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.24 us: 1.07x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.82 ms: 1.09x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.00 us: 1.09x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 73.6 ms: 1.10x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.1 us: 1.11x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.03 us: 1.12x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.05 ms: 1.12x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 62.3 ms: 1.12x slower                                                      |
| scimark_fft              | 187 ms                                                      | 212 ms: 1.13x slower                                                       |
| bench_thread_pool        | 958 us                                                      | 1.08 ms: 1.13x slower                                                      |
| json_loads               | 14.0 us                                                     | 16.0 us: 1.14x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 87.2 ms: 1.15x slower                                                      |
| async_generators         | 222 ms                                                      | 258 ms: 1.16x slower                                                       |
| fannkuch                 | 256 ms                                                      | 298 ms: 1.17x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 73.4 ms: 1.18x slower                                                      |
| pickle                   | 6.85 us                                                     | 8.17 us: 1.19x slower                                                      |
| nbody                    | 71.3 ms                                                     | 85.1 ms: 1.19x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 21.6 us: 1.26x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.97 ms: 1.26x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.05 ms: 1.31x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.66 sec: 1.36x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.31 sec: 1.38x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.74 sec: 1.43x slower                                                     |
| coverage                 | 39.0 ms                                                     | 66.4 ms: 1.70x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (2): genshi_text, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250920-3.15.0a0-20d5494-NOGIL/bm-20250920-pythonperf1-amd64-python-20d5494c88985beb925b-3.15.0a0-20d5494.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.166x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown