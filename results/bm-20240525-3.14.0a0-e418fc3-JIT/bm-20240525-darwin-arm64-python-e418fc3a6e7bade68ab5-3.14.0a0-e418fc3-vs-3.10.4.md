# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: darwin-arm64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 0.75x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 172 ms: 1.12x faster                                                  |
| chameleon      | 6.26 ms                                                | 4.42 ms: 1.41x faster                                                 |
| docutils       | 1.73 sec                                               | 1.51 sec: 1.15x faster                                                |
| html5lib       | 42.4 ms                                                | 31.0 ms: 1.37x faster                                                 |
| tornado_http   | 86.7 ms                                                | 67.4 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 216 ms: 1.80x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 266 ms: 1.78x faster                                                  |
| async_tree_io           | 980 ms                                                 | 580 ms: 1.69x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 473 ms: 1.37x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.65x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 47.3 ms: 1.46x faster                                                 |
| nbody          | 93.0 ms                                                | 63.7 ms: 1.46x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 72.4 ms: 1.31x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.5 ms: 1.02x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.57 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 172 us: 1.63x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.47x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.26 sec: 1.35x faster                                                |
| json_dumps           | 8.11 ms                                                | 6.19 ms: 1.31x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 35.7 ms: 1.30x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 51.2 ms: 1.05x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 70.2 ms: 1.03x faster                                                 |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                 |
| unpickle             | 8.80 us                                                | 9.27 us: 1.05x slower                                                 |
| pickle               | 6.97 us                                                | 7.44 us: 1.07x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.89 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.9 ms: 1.46x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.3 ms: 1.68x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.56x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.37 ms: 1.55x faster                                                 |
| django_template | 26.4 ms                                                | 21.5 ms: 1.23x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.3 ms: 1.06x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 39.3 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.5 us: 3.38x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.46 ms: 2.00x faster                                                 |
| raytrace                 | 301 ms                                                 | 162 ms: 1.86x faster                                                  |
| logging_silent           | 117 ns                                                 | 62.9 ns: 1.86x faster                                                 |
| async_tree_none          | 388 ms                                                 | 216 ms: 1.80x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 266 ms: 1.78x faster                                                  |
| async_tree_io            | 980 ms                                                 | 580 ms: 1.69x faster                                                  |
| chaos                    | 65.8 ms                                                | 39.2 ms: 1.68x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 172 us: 1.63x faster                                                  |
| richards_super           | 57.8 ms                                                | 35.6 ms: 1.62x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 21.6 us: 1.61x faster                                                 |
| mako                     | 9.87 ms                                                | 6.37 ms: 1.55x faster                                                 |
| richards                 | 48.7 ms                                                | 31.7 ms: 1.53x faster                                                 |
| pylint                   | 277 ms                                                 | 182 ms: 1.52x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 826 us: 1.51x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 440 ms: 1.50x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 44.3 ms: 1.48x faster                                                 |
| go                       | 151 ms                                                 | 102 ms: 1.47x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.47x faster                                                  |
| float                    | 69.0 ms                                                | 47.3 ms: 1.46x faster                                                 |
| nbody                    | 93.0 ms                                                | 63.7 ms: 1.46x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.05 us: 1.46x faster                                                 |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.00 ms: 1.44x faster                                                 |
| chameleon                | 6.26 ms                                                | 4.42 ms: 1.41x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.3 ms: 1.41x faster                                                 |
| generators               | 32.3 ms                                                | 23.0 ms: 1.40x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 457 ms: 1.40x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.43 ms: 1.40x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 940 ms: 1.39x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 52.0 ms: 1.38x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.38x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 473 ms: 1.37x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.0 ms: 1.37x faster                                                 |
| pyflate                  | 427 ms                                                 | 315 ms: 1.36x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.26 sec: 1.35x faster                                                |
| thrift                   | 572 us                                                 | 433 us: 1.32x faster                                                  |
| scimark_lu               | 103 ms                                                 | 78.1 ms: 1.32x faster                                                 |
| pycparser                | 877 ms                                                 | 666 ms: 1.32x faster                                                  |
| regex_compile            | 95.3 ms                                                | 72.4 ms: 1.31x faster                                                 |
| deepcopy                 | 272 us                                                 | 207 us: 1.31x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.19 ms: 1.31x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 35.7 ms: 1.30x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.29x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.81 us: 1.29x faster                                                 |
| tornado_http             | 86.7 ms                                                | 67.4 ms: 1.29x faster                                                 |
| scimark_sor              | 128 ms                                                 | 100 ms: 1.28x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 73.1 ms: 1.26x faster                                                 |
| fannkuch                 | 303 ms                                                 | 244 ms: 1.24x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.23x faster                                                |
| django_template          | 26.4 ms                                                | 21.5 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                  |
| sympy_str                | 165 ms                                                 | 137 ms: 1.20x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 10.9 ms: 1.20x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.92 ms: 1.17x faster                                                 |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.51 sec: 1.15x faster                                                |
| sympy_expand             | 269 ms                                                 | 237 ms: 1.14x faster                                                  |
| dask                     | 253 ms                                                 | 224 ms: 1.13x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 32.9 ms: 1.12x faster                                                 |
| 2to3                     | 192 ms                                                 | 172 ms: 1.12x faster                                                  |
| nqueens                  | 63.8 ms                                                | 57.4 ms: 1.11x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 480 us: 1.10x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.5 ms: 1.09x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.51 sec: 1.08x faster                                                |
| meteor_contest           | 77.7 ms                                                | 72.5 ms: 1.07x faster                                                 |
| genshi_text              | 17.3 ms                                                | 16.3 ms: 1.06x faster                                                 |
| json                     | 3.08 ms                                                | 2.91 ms: 1.06x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 51.2 ms: 1.05x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 70.2 ms: 1.03x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.5 ms: 1.02x slower                                                 |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.57 ms: 1.05x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.05x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.27 us: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 908 us: 1.06x slower                                                  |
| pickle                   | 6.97 us                                                | 7.44 us: 1.07x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.56 us: 1.07x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.89 us: 1.07x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.5 ms: 1.10x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 39.3 ms: 1.16x slower                                                 |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                                  |
| telco                    | 3.49 ms                                                | 4.59 ms: 1.32x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 49.9 ms: 1.34x slower                                                 |
| flaskblogging            | 2.65 ms                                                | 3.57 ms: 1.35x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.9 ms: 1.46x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.3 ms: 1.68x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (12) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 0.75x