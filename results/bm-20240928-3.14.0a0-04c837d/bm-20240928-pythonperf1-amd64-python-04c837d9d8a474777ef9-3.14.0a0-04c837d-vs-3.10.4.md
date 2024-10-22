# Results vs. 3.10.4

- fork: python
- ref: 04c837d9d8a474777ef9
- machine: windows-amd64
- commit hash: 04c837d
- commit date: 2024-09-28
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                     |
| html5lib       | 51.0 ms                                                     | 40.8 ms: 1.25x faster                                                      |
| tornado_http   | 108 ms                                                      | 92.7 ms: 1.17x faster                                                      |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 211 ms: 2.07x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 262 ms: 2.01x faster                                                       |
| async_tree_io           | 1.11 sec                                                    | 576 ms: 1.92x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 387 ms: 1.65x faster                                                       |
| Geometric mean          | (ref)                                                       | 1.90x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.2 ms: 1.10x faster                                                      |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| nbody          | 71.3 ms                                                     | 89.4 ms: 1.25x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| regex_compile  | 106 ms                                                      | 92.9 ms: 1.14x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.43 ms: 1.43x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 221 us: 1.22x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 156 us: 1.17x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.6 ms: 1.07x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.6 ms: 1.03x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| unpickle             | 9.09 us                                                     | 9.24 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.1 ms: 1.02x slower                                                      |
| pickle               | 6.85 us                                                     | 7.19 us: 1.05x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 58.4 ms: 1.05x slower                                                      |
| unpickle_list        | 2.71 us                                                     | 2.86 us: 1.05x slower                                                      |
| pickle_dict          | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| pickle_list          | 2.75 us                                                     | 3.01 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.88 ms: 1.31x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.8 ms: 1.15x faster                                                      |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.08x faster                                                       |
| async_tree_none          | 435 ms                                                      | 211 ms: 2.07x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 262 ms: 2.01x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 576 ms: 1.92x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.32 ms: 1.80x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 387 ms: 1.65x faster                                                       |
| generators               | 32.4 ms                                                     | 20.6 ms: 1.57x faster                                                      |
| pylint                   | 350 ms                                                      | 225 ms: 1.56x faster                                                       |
| go                       | 139 ms                                                      | 89.7 ms: 1.55x faster                                                      |
| logging_silent           | 94.6 ns                                                     | 65.4 ns: 1.45x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.43 ms: 1.43x faster                                                      |
| richards_super           | 52.2 ms                                                     | 37.4 ms: 1.40x faster                                                      |
| raytrace                 | 273 ms                                                      | 196 ms: 1.40x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 526 ms: 1.39x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                      |
| deepcopy                 | 255 us                                                      | 190 us: 1.35x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.3 us: 1.34x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 906 us: 1.34x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.58 sec: 1.34x faster                                                     |
| deepcopy_memo            | 28.8 us                                                     | 21.6 us: 1.33x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.88 ms: 1.31x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.30x faster                                                      |
| richards                 | 42.4 ms                                                     | 33.3 ms: 1.27x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 49.4 ms: 1.27x faster                                                      |
| pycparser                | 930 ms                                                      | 735 ms: 1.27x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 68.1 ms: 1.26x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 40.8 ms: 1.25x faster                                                      |
| pyflate                  | 409 ms                                                      | 330 ms: 1.24x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.70 ms: 1.22x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 221 us: 1.22x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.5 ms: 1.18x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 156 us: 1.17x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                                      |
| tornado_http             | 108 ms                                                      | 92.7 ms: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 825 us: 1.16x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                      |
| thrift                   | 617 us                                                      | 535 us: 1.15x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.9 ms: 1.15x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.8 ms: 1.15x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.55 sec: 1.15x faster                                                     |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                      |
| regex_compile            | 106 ms                                                      | 92.9 ms: 1.14x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                     |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 69.2 ms: 1.12x faster                                                      |
| scimark_sor              | 106 ms                                                      | 95.5 ms: 1.11x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 51.6 ms: 1.11x faster                                                      |
| float                    | 61.7 ms                                                     | 56.2 ms: 1.10x faster                                                      |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.8 ms: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.9 ms: 1.07x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 41.6 ms: 1.07x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                                     |
| sqlglot_normalize        | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 564 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.6 ms: 1.03x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.03x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| sympy_expand             | 314 ms                                                      | 310 ms: 1.01x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.8 ms: 1.01x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                      |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                       |
| unpickle                 | 9.09 us                                                     | 9.24 us: 1.02x slower                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.1 ms: 1.02x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.90 us: 1.02x slower                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.80 ms: 1.03x slower                                                      |
| logging_simple           | 6.22 us                                                     | 6.47 us: 1.04x slower                                                      |
| pickle                   | 6.85 us                                                     | 7.19 us: 1.05x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 58.4 ms: 1.05x slower                                                      |
| meteor_contest           | 75.9 ms                                                     | 79.9 ms: 1.05x slower                                                      |
| unpickle_list            | 2.71 us                                                     | 2.86 us: 1.05x slower                                                      |
| pathlib                  | 75.7 ms                                                     | 80.2 ms: 1.06x slower                                                      |
| pickle_dict              | 17.2 us                                                     | 18.5 us: 1.08x slower                                                      |
| python_startup           | 20.6 ms                                                     | 22.2 ms: 1.08x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 1.54 ms: 1.09x slower                                                      |
| pickle_list              | 2.75 us                                                     | 3.01 us: 1.09x slower                                                      |
| scimark_fft              | 187 ms                                                      | 205 ms: 1.10x slower                                                       |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 889 us: 1.11x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 69.1 ms: 1.11x slower                                                      |
| unpack_sequence          | 39.6 ns                                                     | 45.8 ns: 1.16x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                      |
| fannkuch                 | 256 ms                                                      | 308 ms: 1.20x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.7 ms: 1.22x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.91 ms: 1.25x slower                                                      |
| nbody                    | 71.3 ms                                                     | 89.4 ms: 1.25x slower                                                      |
| json                     | 3.14 ms                                                     | 4.24 ms: 1.35x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                               |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240928-3.14.0a0-04c837d/bm-20240928-pythonperf1-amd64-python-04c837d9d8a474777ef9-3.14.0a0-04c837d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown