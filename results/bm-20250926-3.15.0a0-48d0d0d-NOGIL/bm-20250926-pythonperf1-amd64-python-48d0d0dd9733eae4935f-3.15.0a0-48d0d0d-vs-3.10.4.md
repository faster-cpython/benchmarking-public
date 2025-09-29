# Results vs. 3.10.4

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: windows-amd64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.189x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                       |
| docutils       | 1.92 sec                                                    | 2.81 sec: 1.47x slower                                                     |
| html5lib       | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                      |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 339 ms: 3.27x faster                                                       |
| async_tree_none         | 435 ms                                                      | 168 ms: 2.59x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.55x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                      |
| pidigits       | 149 ms                                                      | 137 ms: 1.09x faster                                                       |
| nbody          | 71.3 ms                                                     | 78.5 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| regex_compile  | 106 ms                                                      | 90.6 ms: 1.17x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.06 ms: 1.51x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 223 us: 1.21x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 57.3 ms: 1.13x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 90.7 ms: 1.07x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 43.2 ms: 1.03x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 60.6 ms: 1.09x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.02 us: 1.10x slower                                                      |
| unpickle             | 9.09 us                                                     | 10.3 us: 1.13x slower                                                      |
| pickle               | 6.85 us                                                     | 7.84 us: 1.14x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 3.12 us: 1.15x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 20.0 us: 1.17x slower                                                      |
| json_loads           | 14.0 us                                                     | 16.5 us: 1.17x slower                                                      |
| tomli_loads          | 1.67 sec                                                    | 2.31 sec: 1.38x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 25.9 ms: 1.12x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.5 ms: 1.07x faster                                                      |
| mako            | 9.03 ms                                                     | 9.65 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 339 ms: 3.27x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 28.7 ms: 2.64x faster                                                      |
| typing_runtime_protocols | 336 us                                                      | 128 us: 2.62x faster                                                       |
| async_tree_none          | 435 ms                                                      | 168 ms: 2.59x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.36 ms: 1.78x faster                                                      |
| pylint                   | 350 ms                                                      | 204 ms: 1.71x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.06 sec: 1.67x faster                                                     |
| logging_silent           | 94.6 ns                                                     | 60.0 ns: 1.58x faster                                                      |
| go                       | 139 ms                                                      | 88.5 ms: 1.57x faster                                                      |
| generators               | 32.4 ms                                                     | 20.7 ms: 1.56x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.8 us: 1.53x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.06 ms: 1.51x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.3 us: 1.46x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.33 us: 1.44x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.9 ms: 1.41x faster                                                      |
| deepcopy                 | 255 us                                                      | 182 us: 1.40x faster                                                       |
| chaos                    | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                      |
| float                    | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 540 ms: 1.36x faster                                                       |
| pyflate                  | 409 ms                                                      | 302 ms: 1.36x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 63.5 ms: 1.35x faster                                                      |
| pycparser                | 930 ms                                                      | 692 ms: 1.35x faster                                                       |
| richards                 | 42.4 ms                                                     | 31.6 ms: 1.34x faster                                                      |
| raytrace                 | 273 ms                                                      | 210 ms: 1.30x faster                                                       |
| scimark_sor              | 106 ms                                                      | 82.2 ms: 1.29x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.45 ms: 1.29x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.4 ms: 1.22x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 223 us: 1.21x faster                                                       |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 33.8 ns: 1.17x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.9 ms: 1.17x faster                                                      |
| regex_compile            | 106 ms                                                      | 90.6 ms: 1.17x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.23 ms: 1.15x faster                                                      |
| sympy_sum                | 107 ms                                                      | 94.1 ms: 1.14x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 57.3 ms: 1.13x faster                                                      |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.12x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.11x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 56.5 ms: 1.11x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.99 us: 1.10x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 540 ms: 1.10x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 70.5 ms: 1.10x faster                                                      |
| pidigits                 | 149 ms                                                      | 137 ms: 1.09x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 37.6 ms: 1.09x faster                                                      |
| thrift                   | 617 us                                                      | 569 us: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 181 ms: 1.07x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.5 ms: 1.07x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 90.7 ms: 1.07x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 43.2 ms: 1.03x faster                                                      |
| sympy_expand             | 314 ms                                                      | 311 ms: 1.01x faster                                                       |
| json                     | 3.14 ms                                                     | 3.11 ms: 1.01x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.37 us: 1.02x slower                                                      |
| logging_format           | 6.76 us                                                     | 7.10 us: 1.05x slower                                                      |
| mako                     | 9.03 ms                                                     | 9.65 ms: 1.07x slower                                                      |
| nqueens                  | 66.6 ms                                                     | 71.4 ms: 1.07x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.94 ms: 1.08x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 60.6 ms: 1.09x slower                                                      |
| bench_thread_pool        | 958 us                                                      | 1.05 ms: 1.10x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.02 us: 1.10x slower                                                      |
| nbody                    | 71.3 ms                                                     | 78.5 ms: 1.10x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 85.8 ms: 1.13x slower                                                      |
| unpickle                 | 9.09 us                                                     | 10.3 us: 1.13x slower                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.40 sec: 1.14x slower                                                     |
| pickle                   | 6.85 us                                                     | 7.84 us: 1.14x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 3.12 us: 1.15x slower                                                      |
| async_generators         | 222 ms                                                      | 255 ms: 1.15x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.0 us: 1.17x slower                                                      |
| json_loads               | 14.0 us                                                     | 16.5 us: 1.17x slower                                                      |
| fannkuch                 | 256 ms                                                      | 302 ms: 1.18x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 74.7 ms: 1.20x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.5 ms: 1.24x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.00 ms: 1.25x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.00 ms: 1.27x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.61 sec: 1.32x slower                                                     |
| tomli_loads              | 1.67 sec                                                    | 2.31 sec: 1.38x slower                                                     |
| docutils                 | 1.92 sec                                                    | 2.81 sec: 1.47x slower                                                     |
| coverage                 | 39.0 ms                                                     | 66.8 ms: 1.71x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (2): regex_effbot, scimark_fft
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250926-3.15.0a0-48d0d0d-NOGIL/bm-20250926-pythonperf1-amd64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.189x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown