# Results vs. 3.10.4

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.316x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.17x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                                       |
| async_tree_none         | 435 ms                                                      | 168 ms: 2.60x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 205 ms: 2.57x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.8 ms: 1.44x faster                                                      |
| nbody          | 71.3 ms                                                     | 52.3 ms: 1.36x faster                                                      |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.6 ms: 1.35x faster                                                      |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 106 us: 1.73x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.11 sec: 1.51x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.11 ms: 1.50x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 203 us: 1.33x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 86.8 ms: 1.12x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.73 us: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.8 ms: 1.03x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.55 us: 1.10x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 19.3 us: 1.13x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.30 us: 1.20x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.44 ms: 1.66x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.24x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                                       |
| async_tree_none          | 435 ms                                                      | 168 ms: 2.60x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 205 ms: 2.57x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.9 ms: 2.38x faster                                                      |
| mdp                      | 1.78 sec                                                    | 798 ms: 2.23x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.13 ms: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                       |
| go                       | 139 ms                                                      | 75.0 ms: 1.85x faster                                                      |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.2 ns: 1.75x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 106 us: 1.73x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.3 ms: 1.72x faster                                                      |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.44 ms: 1.66x faster                                                      |
| pyflate                  | 409 ms                                                      | 252 ms: 1.62x faster                                                       |
| richards                 | 42.4 ms                                                     | 26.4 ms: 1.61x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                                      |
| chaos                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                                      |
| raytrace                 | 273 ms                                                      | 177 ms: 1.54x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.9 us: 1.52x faster                                                      |
| deepcopy                 | 255 us                                                      | 168 us: 1.52x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.11 sec: 1.51x faster                                                     |
| json_dumps               | 9.16 ms                                                     | 6.11 ms: 1.50x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.46x faster                                                     |
| float                    | 61.7 ms                                                     | 42.8 ms: 1.44x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 60.7 ms: 1.41x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.06 ms: 1.41x faster                                                      |
| scimark_sor              | 106 ms                                                      | 75.2 ms: 1.41x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.3 ms: 1.39x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 528 ms: 1.39x faster                                                       |
| nbody                    | 71.3 ms                                                     | 52.3 ms: 1.36x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.3 ms: 1.35x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.6 ms: 1.35x faster                                                      |
| pycparser                | 930 ms                                                      | 696 ms: 1.34x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.3 ms: 1.33x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 203 us: 1.33x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 449 ms: 1.32x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 927 ms: 1.32x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| thrift                   | 617 us                                                      | 486 us: 1.27x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 62.1 ms: 1.24x faster                                                      |
| scimark_fft              | 187 ms                                                      | 151 ms: 1.24x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.8 ms: 1.24x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.5 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.27 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.17x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.65 us: 1.16x faster                                                      |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                       |
| fannkuch                 | 256 ms                                                      | 224 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                       |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 851 us: 1.13x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.6 ms: 1.12x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 86.8 ms: 1.12x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 36.5 ns: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.07x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.0 ms: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.73 us: 1.04x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.8 ms: 1.03x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.61 us: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.12 us: 1.02x faster                                                      |
| json                     | 3.14 ms                                                     | 3.11 ms: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.25 ms: 1.08x slower                                                      |
| async_generators         | 222 ms                                                      | 244 ms: 1.10x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.55 us: 1.10x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 19.3 us: 1.13x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.30 us: 1.20x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.6 ms: 1.32x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.16 ms: 1.54x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 95.3 ms: 1.54x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250705-3.15.0a0-1953713-JIT/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.316x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown