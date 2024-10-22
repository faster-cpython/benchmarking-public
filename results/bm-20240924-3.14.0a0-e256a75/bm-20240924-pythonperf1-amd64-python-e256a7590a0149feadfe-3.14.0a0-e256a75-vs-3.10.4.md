# Results vs. 3.10.4

- fork: python
- ref: e256a7590a0149feadfe
- machine: windows-amd64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.5 ms: 1.26x faster                                                      |
| tornado_http   | 108 ms                                                      | 83.1 ms: 1.30x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 207 ms: 2.10x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 566 ms: 1.96x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 386 ms: 1.65x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.2 ms: 1.12x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 83.2 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.4 ms: 1.17x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.35 ms: 1.44x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 149 us: 1.23x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| xml_etree_parse      | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| pickle               | 6.85 us                                                     | 7.04 us: 1.03x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.39 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.05x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.96 us: 1.08x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.81 ms: 1.33x faster                                                      |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.0 ms: 1.16x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.06x faster                                                       |
| async_tree_none          | 435 ms                                                      | 207 ms: 2.10x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 261 ms: 2.02x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 566 ms: 1.96x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 386 ms: 1.65x faster                                                       |
| go                       | 139 ms                                                      | 86.6 ms: 1.60x faster                                                      |
| pylint                   | 350 ms                                                      | 224 ms: 1.57x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 471 ms: 1.55x faster                                                       |
| generators               | 32.4 ms                                                     | 21.0 ms: 1.54x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 63.8 ns: 1.48x faster                                                      |
| chaos                    | 61.7 ms                                                     | 42.7 ms: 1.45x faster                                                      |
| raytrace                 | 273 ms                                                      | 189 ms: 1.44x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.35 ms: 1.44x faster                                                      |
| richards_super           | 52.2 ms                                                     | 36.4 ms: 1.43x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.48 sec: 1.42x faster                                                     |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.8 us: 1.38x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 62.5 ms: 1.37x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 888 us: 1.37x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.81 ms: 1.33x faster                                                      |
| deepcopy                 | 255 us                                                      | 193 us: 1.33x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.3 ms: 1.31x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.8 ms: 1.31x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.39 ms: 1.31x faster                                                      |
| tornado_http             | 108 ms                                                      | 83.1 ms: 1.30x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                       |
| pyflate                  | 409 ms                                                      | 322 ms: 1.27x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.5 ms: 1.26x faster                                                      |
| pycparser                | 930 ms                                                      | 740 ms: 1.26x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                                     |
| unpickle_pure_python     | 183 us                                                      | 149 us: 1.23x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 802 us: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.7 ms: 1.19x faster                                                      |
| thrift                   | 617 us                                                      | 523 us: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.8 ms: 1.18x faster                                                      |
| regex_compile            | 106 ms                                                      | 90.4 ms: 1.17x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.0 ms: 1.17x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.16x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 17.0 ms: 1.16x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.4 ms: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| scimark_sor              | 106 ms                                                      | 93.1 ms: 1.14x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.14x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                     |
| float                    | 61.7 ms                                                     | 55.2 ms: 1.12x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 69.8 ms: 1.11x faster                                                      |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 542 ms: 1.09x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                     |
| xml_etree_parse          | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| sympy_expand             | 314 ms                                                      | 306 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.66 ms: 1.02x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.9 ms: 1.02x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 65.5 ms: 1.02x faster                                                      |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.85 us: 1.01x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 40.3 ns: 1.02x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.35 us: 1.02x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.04 us: 1.03x slower                                                      |
| unpickle                 | 9.09 us                                                     | 9.39 us: 1.03x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 78.6 ms: 1.04x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 57.7 ms: 1.04x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.05x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 66.0 ms: 1.06x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.96 us: 1.08x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.53 ms: 1.08x slower                                                      |
| scimark_fft              | 187 ms                                                      | 204 ms: 1.09x slower                                                       |
| async_generators         | 222 ms                                                      | 243 ms: 1.10x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 884 us: 1.11x slower                                                       |
| nbody                    | 71.3 ms                                                     | 83.2 ms: 1.17x slower                                                      |
| fannkuch                 | 256 ms                                                      | 299 ms: 1.17x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.4 ms: 1.19x slower                                                      |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.26x slower                                                      |
| telco                    | 3.94 ms                                                     | 5.09 ms: 1.29x slower                                                      |
| json                     | 3.14 ms                                                     | 4.50 ms: 1.44x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf1-amd64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown