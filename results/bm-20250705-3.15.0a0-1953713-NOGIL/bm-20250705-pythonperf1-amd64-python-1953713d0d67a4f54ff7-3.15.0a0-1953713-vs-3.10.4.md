# Results vs. 3.10.4

- fork: python
- ref: 1953713d0d67a4f54ff7
- machine: windows-amd64
- commit hash: 1953713
- commit date: 2025-07-05
- overall geometric mean: 1.135x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.89 sec: 1.51x slower                                                     |
| html5lib       | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 406 ms: 2.73x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 259 ms: 2.04x faster                                                       |
| async_tree_none         | 435 ms                                                      | 214 ms: 2.03x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 374 ms: 1.71x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.10x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                      |
| pidigits       | 149 ms                                                      | 136 ms: 1.10x faster                                                       |
| nbody          | 71.3 ms                                                     | 83.9 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| regex_compile  | 106 ms                                                      | 93.3 ms: 1.14x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.65 ms: 1.38x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 154 us: 1.19x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 232 us: 1.16x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 58.3 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                      |
| pickle_list          | 2.75 us                                                     | 3.04 us: 1.10x slower                                                      |
| pickle               | 6.85 us                                                     | 7.64 us: 1.12x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.03 us: 1.12x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.0 us: 1.14x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.4 us: 1.14x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 63.5 ms: 1.14x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.2 us: 1.17x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.66 sec: 1.59x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 41.7 ms: 1.02x slower                                                      |
| mako            | 9.03 ms                                                     | 9.81 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 406 ms: 2.73x faster                                                       |
| typing_runtime_protocols | 336 us                                                      | 128 us: 2.63x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.2 ms: 2.35x faster                                                      |
| async_tree_memoization   | 526 ms                                                      | 259 ms: 2.04x faster                                                       |
| async_tree_none          | 435 ms                                                      | 214 ms: 2.03x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.42 ms: 1.73x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 374 ms: 1.71x faster                                                       |
| pylint                   | 350 ms                                                      | 216 ms: 1.62x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.13 sec: 1.58x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 62.3 ns: 1.52x faster                                                      |
| go                       | 139 ms                                                      | 92.4 ms: 1.50x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 496 ms: 1.47x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.33 us: 1.44x faster                                                      |
| generators               | 32.4 ms                                                     | 22.7 ms: 1.43x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.8 us: 1.38x faster                                                      |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.38x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.65 ms: 1.38x faster                                                      |
| chaos                    | 61.7 ms                                                     | 46.3 ms: 1.33x faster                                                      |
| float                    | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                      |
| richards_super           | 52.2 ms                                                     | 40.0 ms: 1.31x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 65.7 ms: 1.31x faster                                                      |
| pyflate                  | 409 ms                                                      | 314 ms: 1.30x faster                                                       |
| raytrace                 | 273 ms                                                      | 210 ms: 1.30x faster                                                       |
| richards                 | 42.4 ms                                                     | 33.2 ms: 1.28x faster                                                      |
| pycparser                | 930 ms                                                      | 729 ms: 1.28x faster                                                       |
| deepcopy                 | 255 us                                                      | 201 us: 1.27x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.56 ms: 1.26x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                      |
| scimark_sor              | 106 ms                                                      | 86.2 ms: 1.23x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.1 ms: 1.20x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 154 us: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 232 us: 1.16x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.22 ms: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.9 ms: 1.15x faster                                                      |
| regex_compile            | 106 ms                                                      | 93.3 ms: 1.14x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 55.8 ms: 1.12x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 58.3 ms: 1.11x faster                                                      |
| sympy_sum                | 107 ms                                                      | 97.4 ms: 1.10x faster                                                      |
| pidigits                 | 149 ms                                                      | 136 ms: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.08x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                      |
| thrift                   | 617 us                                                      | 576 us: 1.07x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 564 ms: 1.05x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 73.8 ms: 1.05x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 38.6 ns: 1.03x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                      |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.03x faster                                                      |
| sympy_str                | 194 ms                                                      | 190 ms: 1.02x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.16 us: 1.02x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 41.7 ms: 1.02x slower                                                      |
| sympy_expand             | 314 ms                                                      | 323 ms: 1.03x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 71.9 ms: 1.08x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.81 ms: 1.09x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.35 us: 1.09x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.04 us: 1.10x slower                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.33 sec: 1.10x slower                                                     |
| logging_simple           | 6.22 us                                                     | 6.89 us: 1.11x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.64 us: 1.12x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.03 us: 1.12x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.08 ms: 1.12x slower                                                      |
| scimark_fft              | 187 ms                                                      | 211 ms: 1.13x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 85.8 ms: 1.13x slower                                                      |
| fannkuch                 | 256 ms                                                      | 291 ms: 1.14x slower                                                       |
| json_loads               | 14.0 us                                                     | 16.0 us: 1.14x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.10 ms: 1.14x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.4 us: 1.14x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 63.5 ms: 1.14x slower                                                      |
| async_generators         | 222 ms                                                      | 257 ms: 1.16x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.2 us: 1.17x slower                                                      |
| nbody                    | 71.3 ms                                                     | 83.9 ms: 1.18x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 79.5 ms: 1.28x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.05 ms: 1.32x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.71 sec: 1.41x slower                                                     |
| telco                    | 3.94 ms                                                     | 5.54 ms: 1.41x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.89 sec: 1.51x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.66 sec: 1.59x slower                                                     |
| coverage                 | 39.0 ms                                                     | 67.1 ms: 1.72x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_process, genshi_text
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250705-3.15.0a0-1953713-NOGIL/bm-20250705-pythonperf1-amd64-python-1953713d0d67a4f54ff7-3.15.0a0-1953713.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.135x faster

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown