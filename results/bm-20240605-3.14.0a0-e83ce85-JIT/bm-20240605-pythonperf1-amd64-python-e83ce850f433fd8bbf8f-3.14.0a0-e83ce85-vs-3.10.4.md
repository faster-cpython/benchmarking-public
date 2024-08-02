# Results vs. 3.10.4

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: windows-amd64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                     |
| html5lib       | 51.0 ms                                                     | 36.8 ms: 1.39x faster                                                      |
| tornado_http   | 108 ms                                                      | 86.2 ms: 1.26x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization  | 526 ms                                                      | 277 ms: 1.90x faster                                                       |
| async_tree_none         | 435 ms                                                      | 229 ms: 1.90x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 603 ms: 1.84x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 400 ms: 1.60x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.80x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                      |
| nbody          | 71.3 ms                                                     | 53.1 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                       | 1.23x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.3 ms: 1.20x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.5 ms: 1.06x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.75 ms: 1.59x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 172 us: 1.56x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 129 us: 1.42x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 91.5 ms: 1.06x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.77 us: 1.04x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| pickle_list          | 2.75 us                                                     | 2.73 us: 1.01x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.00x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.82 us: 1.04x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 17.8 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.29 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 21.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.24 ms: 1.72x faster                                                      |
| django_template | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.1 ms: 1.09x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 44.6 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 277 ms: 1.90x faster                                                       |
| async_tree_none          | 435 ms                                                      | 229 ms: 1.90x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 603 ms: 1.84x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 44.2 ms: 1.75x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.24 ms: 1.72x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 55.4 ns: 1.71x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 400 ms: 1.60x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.75 ms: 1.59x faster                                                      |
| pyflate                  | 409 ms                                                      | 257 ms: 1.59x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 172 us: 1.56x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 470 ms: 1.56x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.8 ms: 1.54x faster                                                      |
| raytrace                 | 273 ms                                                      | 178 ms: 1.54x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.1 ms: 1.54x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.7 ms: 1.52x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 41.6 ms: 1.51x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 808 us: 1.50x faster                                                       |
| generators               | 32.4 ms                                                     | 21.6 ms: 1.50x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.41 sec: 1.49x faster                                                     |
| pylint                   | 350 ms                                                      | 235 ms: 1.49x faster                                                       |
| go                       | 139 ms                                                      | 93.8 ms: 1.48x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 129 us: 1.42x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                                      |
| richards                 | 42.4 ms                                                     | 30.1 ms: 1.41x faster                                                      |
| float                    | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 36.8 ms: 1.39x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.38x faster                                                      |
| nbody                    | 71.3 ms                                                     | 53.1 ms: 1.34x faster                                                      |
| pycparser                | 930 ms                                                      | 716 ms: 1.30x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 457 ms: 1.29x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 949 ms: 1.28x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                      |
| tornado_http             | 108 ms                                                      | 86.2 ms: 1.26x faster                                                      |
| scimark_sor              | 106 ms                                                      | 84.7 ms: 1.25x faster                                                      |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 69.1 ms: 1.24x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.67 ms: 1.23x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                      |
| thrift                   | 617 us                                                      | 508 us: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.21x faster                                                      |
| regex_compile            | 106 ms                                                      | 88.3 ms: 1.20x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.20x faster                                                     |
| bench_thread_pool        | 958 us                                                      | 809 us: 1.18x faster                                                       |
| fannkuch                 | 256 ms                                                      | 217 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.2 ms: 1.15x faster                                                      |
| sympy_sum                | 107 ms                                                      | 94.3 ms: 1.13x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.5 ms: 1.10x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.1 ms: 1.09x faster                                                      |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.0 ms: 1.09x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                      |
| json                     | 3.14 ms                                                     | 2.90 ms: 1.08x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                     |
| logging_format           | 6.76 us                                                     | 6.27 us: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                                       |
| deepcopy                 | 255 us                                                      | 239 us: 1.07x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.3 ms: 1.07x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.84 us: 1.07x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.5 ms: 1.06x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 91.5 ms: 1.06x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.10 us: 1.05x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.77 us: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 73.3 ms: 1.04x faster                                                      |
| sympy_expand             | 314 ms                                                      | 309 ms: 1.02x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                      |
| pathlib                  | 75.7 ms                                                     | 74.9 ms: 1.01x faster                                                      |
| pickle_list              | 2.75 us                                                     | 2.73 us: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.00x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.82 us: 1.04x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 17.8 us: 1.04x slower                                                      |
| python_startup           | 20.6 ms                                                     | 21.8 ms: 1.06x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.29 us: 1.06x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 44.6 ms: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.56 ms: 1.11x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 69.3 ms: 1.12x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 908 us: 1.14x slower                                                       |
| async_generators         | 222 ms                                                      | 254 ms: 1.15x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.55 ms: 1.15x slower                                                      |
| coverage                 | 39.0 ms                                                     | 45.8 ms: 1.17x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240605-3.14.0a0-e83ce85-JIT/bm-20240605-pythonperf1-amd64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown