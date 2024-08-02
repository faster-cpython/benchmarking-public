# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: darwin-arm64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.83x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.19x faster                                                  |
| chameleon      | 6.26 ms                                                | 4.33 ms: 1.45x faster                                                 |
| docutils       | 1.73 sec                                               | 1.44 sec: 1.21x faster                                                |
| html5lib       | 42.4 ms                                                | 31.1 ms: 1.36x faster                                                 |
| tornado_http   | 86.7 ms                                                | 66.8 ms: 1.30x faster                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 214 ms: 1.82x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 264 ms: 1.79x faster                                                  |
| async_tree_io           | 980 ms                                                 | 577 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 474 ms: 1.37x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.66x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.9 ms: 1.55x faster                                                 |
| float          | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.3 ms: 1.40x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.7 ms: 1.03x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 180 us: 1.56x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.32 ms: 1.28x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 36.8 ms: 1.26x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.45 sec: 1.17x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 51.8 ms: 1.03x faster                                                 |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                 |
| unpickle             | 8.80 us                                                | 9.28 us: 1.06x slower                                                 |
| pickle               | 6.97 us                                                | 7.36 us: 1.06x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.86 us: 1.06x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.9 ms: 1.37x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.2 ms: 1.54x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.45x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.00 ms: 1.41x faster                                                 |
| django_template | 26.4 ms                                                | 19.6 ms: 1.35x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.8 ms: 1.25x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 29.8 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 91.2 us: 3.54x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.14 ms: 2.29x faster                                                 |
| raytrace                 | 301 ms                                                 | 148 ms: 2.04x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.0 ns: 1.95x faster                                                 |
| chaos                    | 65.8 ms                                                | 35.5 ms: 1.85x faster                                                 |
| async_tree_none          | 388 ms                                                 | 214 ms: 1.82x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 264 ms: 1.79x faster                                                  |
| async_tree_io            | 980 ms                                                 | 577 ms: 1.70x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 732 us: 1.70x faster                                                  |
| richards_super           | 57.8 ms                                                | 34.9 ms: 1.66x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 892 us: 1.62x faster                                                  |
| pylint                   | 277 ms                                                 | 172 ms: 1.61x faster                                                  |
| comprehensions           | 16.9 us                                                | 10.7 us: 1.58x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 421 ms: 1.56x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 180 us: 1.56x faster                                                  |
| nbody                    | 93.0 ms                                                | 59.9 ms: 1.55x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 42.3 ms: 1.55x faster                                                 |
| scimark_lu               | 103 ms                                                 | 66.7 ms: 1.54x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 22.6 us: 1.54x faster                                                 |
| richards                 | 48.7 ms                                                | 31.9 ms: 1.53x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.08 ms: 1.52x faster                                                 |
| go                       | 151 ms                                                 | 100 ms: 1.51x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.03 us: 1.47x faster                                                 |
| logging_format           | 4.83 us                                                | 3.32 us: 1.45x faster                                                 |
| chameleon                | 6.26 ms                                                | 4.33 ms: 1.45x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 49.8 ms: 1.44x faster                                                 |
| generators               | 32.3 ms                                                | 22.8 ms: 1.42x faster                                                 |
| float                    | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.2 ms: 1.41x faster                                                 |
| mako                     | 9.87 ms                                                | 7.00 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 459 ms: 1.40x faster                                                  |
| regex_compile            | 95.3 ms                                                | 68.3 ms: 1.40x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 937 ms: 1.39x faster                                                  |
| pycparser                | 877 ms                                                 | 632 ms: 1.39x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 474 ms: 1.37x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.1 ms: 1.36x faster                                                 |
| thrift                   | 572 us                                                 | 424 us: 1.35x faster                                                  |
| django_template          | 26.4 ms                                                | 19.6 ms: 1.35x faster                                                 |
| deepcopy                 | 272 us                                                 | 202 us: 1.34x faster                                                  |
| scimark_sor              | 128 ms                                                 | 95.4 ms: 1.34x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 69.1 ms: 1.34x faster                                                 |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.79 us: 1.30x faster                                                 |
| coroutines               | 20.7 ms                                                | 15.9 ms: 1.30x faster                                                 |
| tornado_http             | 86.7 ms                                                | 66.8 ms: 1.30x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.32 ms: 1.28x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.4 ms: 1.27x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 36.8 ms: 1.26x faster                                                 |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                                  |
| genshi_text              | 17.3 ms                                                | 13.8 ms: 1.25x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| scimark_fft              | 224 ms                                                 | 181 ms: 1.24x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.79 ms: 1.23x faster                                                 |
| nqueens                  | 63.8 ms                                                | 52.8 ms: 1.21x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.44 sec: 1.21x faster                                                |
| 2to3                     | 192 ms                                                 | 160 ms: 1.19x faster                                                  |
| sympy_expand             | 269 ms                                                 | 227 ms: 1.19x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.0 ms: 1.19x faster                                                 |
| fannkuch                 | 303 ms                                                 | 257 ms: 1.18x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.45 sec: 1.17x faster                                                |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| dask                     | 253 ms                                                 | 221 ms: 1.15x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 463 us: 1.14x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 29.8 ms: 1.14x faster                                                 |
| pathlib                  | 24.5 ms                                                | 21.9 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 70.4 ms: 1.10x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.48 sec: 1.10x faster                                                |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 51.8 ms: 1.03x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                 |
| regex_v8                 | 17.1 ms                                                | 17.7 ms: 1.03x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 900 us: 1.05x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.28 us: 1.06x slower                                                 |
| pickle                   | 6.97 us                                                | 7.36 us: 1.06x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.86 us: 1.06x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.3 ms: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 279 ms: 1.21x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 46.5 ms: 1.24x slower                                                 |
| flaskblogging            | 2.65 ms                                                | 3.35 ms: 1.27x slower                                                 |
| telco                    | 3.49 ms                                                | 4.53 ms: 1.30x slower                                                 |
| python_startup           | 10.9 ms                                                | 14.9 ms: 1.37x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.2 ms: 1.54x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (12) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.83x