# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 241 ms: 1.02x faster                                                       |
| html5lib       | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                                      |
| tornado_http   | 108 ms                                                      | 87.6 ms: 1.24x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 206 ms: 2.12x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 260 ms: 2.02x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 584 ms: 1.90x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 395 ms: 1.61x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.5 ms: 1.44x faster                                                      |
| float          | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                      |
| Geometric mean | (ref)                                                       | 1.26x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| regex_compile  | 106 ms                                                      | 95.0 ms: 1.12x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.87 ms: 1.56x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 191 us: 1.41x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 142 us: 1.29x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.4 ms: 1.26x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 49.4 ms: 1.12x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.5 ms: 1.04x faster                                                      |
| unpickle             | 9.09 us                                                     | 8.89 us: 1.02x faster                                                      |
| pickle_dict          | 17.2 us                                                     | 17.6 us: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle               | 6.85 us                                                     | 7.19 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.1 ms: 1.07x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.3 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.21 ms: 1.73x faster                                                      |
| django_template | 28.9 ms                                                     | 26.9 ms: 1.07x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 18.8 ms: 1.05x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 44.1 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.81 ms: 2.32x faster                                                      |
| async_tree_none          | 435 ms                                                      | 206 ms: 2.12x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 260 ms: 2.02x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 584 ms: 1.90x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.5 us: 1.86x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 44.1 ms: 1.75x faster                                                      |
| scimark_sor              | 106 ms                                                      | 61.2 ms: 1.74x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.21 ms: 1.73x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 56.7 ns: 1.67x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 38.7 ms: 1.62x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 395 ms: 1.61x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.0 ms: 1.59x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.87 ms: 1.56x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                      |
| chaos                    | 61.7 ms                                                     | 40.0 ms: 1.54x faster                                                      |
| pyflate                  | 409 ms                                                      | 265 ms: 1.54x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.37 sec: 1.54x faster                                                     |
| asyncio_tcp              | 732 ms                                                      | 480 ms: 1.52x faster                                                       |
| go                       | 139 ms                                                      | 91.3 ms: 1.52x faster                                                      |
| nbody                    | 71.3 ms                                                     | 49.5 ms: 1.44x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 191 us: 1.41x faster                                                       |
| generators               | 32.4 ms                                                     | 23.1 ms: 1.40x faster                                                      |
| float                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                                      |
| deepcopy                 | 255 us                                                      | 184 us: 1.38x faster                                                       |
| raytrace                 | 273 ms                                                      | 197 ms: 1.38x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 880 us: 1.38x faster                                                       |
| richards_super           | 52.2 ms                                                     | 38.6 ms: 1.35x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.9 ms: 1.34x faster                                                      |
| pylint                   | 350 ms                                                      | 264 ms: 1.33x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.27 sec: 1.31x faster                                                     |
| pycparser                | 930 ms                                                      | 709 ms: 1.31x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.09 ms: 1.30x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 142 us: 1.29x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.15 ms: 1.28x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.26x faster                                                     |
| xml_etree_process        | 44.5 ms                                                     | 35.4 ms: 1.26x faster                                                      |
| scimark_fft              | 187 ms                                                      | 150 ms: 1.25x faster                                                       |
| tornado_http             | 108 ms                                                      | 87.6 ms: 1.24x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 41.9 ms: 1.22x faster                                                      |
| thrift                   | 617 us                                                      | 513 us: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 803 us: 1.19x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.6 ms: 1.18x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.87 ms: 1.18x faster                                                      |
| richards                 | 42.4 ms                                                     | 36.1 ms: 1.18x faster                                                      |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 503 ms: 1.18x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.04 sec: 1.17x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.4 ms: 1.12x faster                                                      |
| regex_compile            | 106 ms                                                      | 95.0 ms: 1.12x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.09x faster                                                      |
| sympy_sum                | 107 ms                                                      | 98.3 ms: 1.09x faster                                                      |
| fannkuch                 | 256 ms                                                      | 238 ms: 1.08x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.9 ms: 1.07x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.4 ms: 1.07x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.9 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 18.8 ms: 1.05x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.52 us: 1.04x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 14.8 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.5 ms: 1.04x faster                                                      |
| sympy_str                | 194 ms                                                      | 188 ms: 1.03x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.5 ms: 1.03x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.04 us: 1.03x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 201 ms: 1.02x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.89 us: 1.02x faster                                                      |
| 2to3                     | 246 ms                                                      | 241 ms: 1.02x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 40.3 ms: 1.01x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 17.6 us: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.83 us: 1.04x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.19 us: 1.05x slower                                                      |
| sympy_expand             | 314 ms                                                      | 330 ms: 1.05x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 44.1 ms: 1.07x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.1 ms: 1.07x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.54 ms: 1.09x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 899 us: 1.12x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 71.7 ms: 1.16x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.3 ms: 1.18x slower                                                      |
| async_generators         | 222 ms                                                      | 261 ms: 1.18x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.1 ms: 1.18x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.73 ms: 1.20x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 58.0 ns: 1.46x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                               |

Benchmark hidden because not significant (5): docutils, pidigits, pickle_list, pathlib, regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown