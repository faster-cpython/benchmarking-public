# Results vs. 3.10.4

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: windows-amd64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 243 ms: 1.01x faster                                                       |
| html5lib       | 51.0 ms                                                     | 41.5 ms: 1.23x faster                                                      |
| tornado_http   | 108 ms                                                      | 97.3 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 206 ms: 2.11x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 259 ms: 2.03x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 584 ms: 1.90x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 390 ms: 1.63x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.91x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 49.2 ms: 1.45x faster                                                      |
| float          | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                      |
| Geometric mean | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 123 ms: 1.11x faster                                                       |
| regex_compile  | 106 ms                                                      | 96.5 ms: 1.10x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.84 ms: 1.57x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 198 us: 1.36x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                     |
| unpickle_pure_python | 183 us                                                      | 141 us: 1.30x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.0 ms: 1.27x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 49.9 ms: 1.11x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.9 ms: 1.04x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 17.7 us: 1.03x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.82 us: 1.04x slower                                                      |
| pickle_list          | 2.75 us                                                     | 2.88 us: 1.05x slower                                                      |
| pickle               | 6.85 us                                                     | 7.31 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.5 ms: 1.09x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.3 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 4.92 ms: 1.83x faster                                                      |
| django_template | 28.9 ms                                                     | 26.8 ms: 1.08x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 45.5 ms: 1.11x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.09x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.84 ms: 2.27x faster                                                      |
| async_tree_none          | 435 ms                                                      | 206 ms: 2.11x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 259 ms: 2.03x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 584 ms: 1.90x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 15.5 us: 1.85x faster                                                      |
| mako                     | 9.03 ms                                                     | 4.92 ms: 1.83x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 43.8 ms: 1.76x faster                                                      |
| scimark_sor              | 106 ms                                                      | 61.1 ms: 1.74x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 390 ms: 1.63x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 38.7 ms: 1.62x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 58.9 ns: 1.61x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.84 ms: 1.57x faster                                                      |
| pyflate                  | 409 ms                                                      | 265 ms: 1.55x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 55.6 ms: 1.54x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.54x faster                                                      |
| go                       | 139 ms                                                      | 93.2 ms: 1.49x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.7 ms: 1.48x faster                                                      |
| nbody                    | 71.3 ms                                                     | 49.2 ms: 1.45x faster                                                      |
| generators               | 32.4 ms                                                     | 22.9 ms: 1.41x faster                                                      |
| float                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.53 sec: 1.38x faster                                                     |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 198 us: 1.36x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 896 us: 1.36x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 542 ms: 1.35x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 42.8 ms: 1.34x faster                                                      |
| richards_super           | 52.2 ms                                                     | 39.3 ms: 1.33x faster                                                      |
| raytrace                 | 273 ms                                                      | 207 ms: 1.32x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                     |
| pylint                   | 350 ms                                                      | 268 ms: 1.31x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 141 us: 1.30x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.0 ms: 1.27x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.16 ms: 1.27x faster                                                      |
| pycparser                | 930 ms                                                      | 736 ms: 1.26x faster                                                       |
| scimark_fft              | 187 ms                                                      | 148 ms: 1.26x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.41 sec: 1.26x faster                                                     |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.20 ms: 1.24x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 41.5 ms: 1.23x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| thrift                   | 617 us                                                      | 518 us: 1.19x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 806 us: 1.19x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.5 ms: 1.16x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 5.03 ms: 1.14x faster                                                      |
| richards                 | 42.4 ms                                                     | 37.3 ms: 1.14x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.13x faster                                                      |
| tornado_http             | 108 ms                                                      | 97.3 ms: 1.11x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.9 ms: 1.11x faster                                                      |
| regex_dna                | 136 ms                                                      | 123 ms: 1.11x faster                                                       |
| regex_compile            | 106 ms                                                      | 96.5 ms: 1.10x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 539 ms: 1.10x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                     |
| django_template          | 28.9 ms                                                     | 26.8 ms: 1.08x faster                                                      |
| sympy_sum                | 107 ms                                                      | 99.7 ms: 1.07x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 62.2 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.41 us: 1.05x faster                                                      |
| fannkuch                 | 256 ms                                                      | 243 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.97 us: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.9 ms: 1.04x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 15.0 ms: 1.02x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| sympy_str                | 194 ms                                                      | 192 ms: 1.01x faster                                                       |
| 2to3                     | 246 ms                                                      | 243 ms: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 75.2 ms: 1.01x faster                                                      |
| sqlglot_normalize        | 205 ms                                                      | 203 ms: 1.01x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 40.8 ms: 1.02x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 17.7 us: 1.03x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.82 us: 1.04x slower                                                      |
| pickle_list              | 2.75 us                                                     | 2.88 us: 1.05x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.31 us: 1.07x slower                                                      |
| sympy_expand             | 314 ms                                                      | 337 ms: 1.07x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 81.6 ms: 1.08x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.5 ms: 1.09x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.55 ms: 1.10x slower                                                      |
| genshi_xml               | 41.0 ms                                                     | 45.5 ms: 1.11x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 895 us: 1.12x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 71.5 ms: 1.15x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.56 ms: 1.16x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.3 ms: 1.18x slower                                                      |
| async_generators         | 222 ms                                                      | 261 ms: 1.18x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.3 ms: 1.21x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 56.3 ns: 1.42x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (4): pidigits, docutils, unpickle, regex_v8
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-pythonperf1-amd64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown