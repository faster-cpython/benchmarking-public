# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_align
- machine: darwin-arm64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 0.80x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 171 ms: 1.12x faster                                                |
| chameleon      | 6.26 ms                                                | 4.44 ms: 1.41x faster                                               |
| docutils       | 1.73 sec                                               | 1.52 sec: 1.14x faster                                              |
| html5lib       | 42.4 ms                                                | 30.8 ms: 1.38x faster                                               |
| tornado_http   | 86.7 ms                                                | 68.0 ms: 1.28x faster                                               |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 216 ms: 1.80x faster                                                |
| async_tree_memoization  | 474 ms                                                 | 266 ms: 1.78x faster                                                |
| async_tree_io           | 980 ms                                                 | 577 ms: 1.70x faster                                                |
| async_tree_cpu_io_mixed | 649 ms                                                 | 475 ms: 1.37x faster                                                |
| Geometric mean          | (ref)                                                  | 1.65x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.5 ms: 1.46x faster                                               |
| float          | 69.0 ms                                                | 47.2 ms: 1.46x faster                                               |
| Geometric mean | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 71.7 ms: 1.33x faster                                               |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.02x slower                                               |
| regex_effbot   | 2.46 ms                                                | 2.57 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 172 us: 1.63x faster                                                |
| unpickle_pure_python | 194 us                                                 | 131 us: 1.48x faster                                                |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.38x faster                                              |
| json_dumps           | 8.11 ms                                                | 6.07 ms: 1.34x faster                                               |
| xml_etree_process    | 46.5 ms                                                | 35.4 ms: 1.31x faster                                               |
| xml_etree_generate   | 53.5 ms                                                | 51.1 ms: 1.05x faster                                               |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                |
| xml_etree_iterparse  | 72.1 ms                                                | 70.1 ms: 1.03x faster                                               |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                               |
| unpickle_list        | 2.69 us                                                | 2.83 us: 1.05x slower                                               |
| unpickle             | 8.80 us                                                | 9.32 us: 1.06x slower                                               |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                               |
| pickle               | 6.97 us                                                | 7.46 us: 1.07x slower                                               |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.7 ms: 1.44x slower                                               |
| python_startup_no_site | 7.91 ms                                                | 13.2 ms: 1.67x slower                                               |
| Geometric mean         | (ref)                                                  | 1.55x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.40 ms: 1.54x faster                                               |
| django_template | 26.4 ms                                                | 21.0 ms: 1.25x faster                                               |
| genshi_text     | 17.3 ms                                                | 16.1 ms: 1.07x faster                                               |
| genshi_xml      | 33.8 ms                                                | 39.5 ms: 1.17x slower                                               |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.5 us: 3.46x faster                                               |
| deltablue                | 4.91 ms                                                | 2.46 ms: 1.99x faster                                               |
| logging_silent           | 117 ns                                                 | 61.8 ns: 1.90x faster                                               |
| raytrace                 | 301 ms                                                 | 162 ms: 1.86x faster                                                |
| async_tree_none          | 388 ms                                                 | 216 ms: 1.80x faster                                                |
| async_tree_memoization   | 474 ms                                                 | 266 ms: 1.78x faster                                                |
| async_tree_io            | 980 ms                                                 | 577 ms: 1.70x faster                                                |
| chaos                    | 65.8 ms                                                | 38.8 ms: 1.70x faster                                               |
| richards_super           | 57.8 ms                                                | 34.9 ms: 1.66x faster                                               |
| pickle_pure_python       | 281 us                                                 | 172 us: 1.63x faster                                                |
| deepcopy_memo            | 34.7 us                                                | 21.4 us: 1.63x faster                                               |
| asyncio_tcp              | 659 ms                                                 | 416 ms: 1.58x faster                                                |
| richards                 | 48.7 ms                                                | 31.2 ms: 1.56x faster                                               |
| mako                     | 9.87 ms                                                | 6.40 ms: 1.54x faster                                               |
| pylint                   | 277 ms                                                 | 184 ms: 1.51x faster                                                |
| sqlglot_parse            | 1.24 ms                                                | 830 us: 1.50x faster                                                |
| scimark_monte_carlo      | 65.6 ms                                                | 43.9 ms: 1.49x faster                                               |
| unpickle_pure_python     | 194 us                                                 | 131 us: 1.48x faster                                                |
| logging_simple           | 4.45 us                                                | 3.03 us: 1.47x faster                                               |
| logging_format           | 4.83 us                                                | 3.29 us: 1.47x faster                                               |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.46x faster                                               |
| float                    | 69.0 ms                                                | 47.2 ms: 1.46x faster                                               |
| go                       | 151 ms                                                 | 103 ms: 1.46x faster                                                |
| sqlglot_transpile        | 1.44 ms                                                | 1.00 ms: 1.44x faster                                               |
| hexiom                   | 6.19 ms                                                | 4.36 ms: 1.42x faster                                               |
| spectral_norm            | 94.8 ms                                                | 67.1 ms: 1.41x faster                                               |
| chameleon                | 6.26 ms                                                | 4.44 ms: 1.41x faster                                               |
| pprint_safe_repr         | 641 ms                                                 | 457 ms: 1.40x faster                                                |
| generators               | 32.3 ms                                                | 23.2 ms: 1.40x faster                                               |
| comprehensions           | 16.9 us                                                | 12.2 us: 1.39x faster                                               |
| crypto_pyaes             | 71.8 ms                                                | 51.9 ms: 1.38x faster                                               |
| pprint_pformat           | 1.30 sec                                               | 947 ms: 1.38x faster                                                |
| html5lib                 | 42.4 ms                                                | 30.8 ms: 1.38x faster                                               |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.38x faster                                              |
| pyflate                  | 427 ms                                                 | 312 ms: 1.37x faster                                                |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 475 ms: 1.37x faster                                                |
| json_dumps               | 8.11 ms                                                | 6.07 ms: 1.34x faster                                               |
| deepcopy                 | 272 us                                                 | 204 us: 1.33x faster                                                |
| regex_compile            | 95.3 ms                                                | 71.7 ms: 1.33x faster                                               |
| thrift                   | 572 us                                                 | 434 us: 1.32x faster                                                |
| scimark_lu               | 103 ms                                                 | 78.2 ms: 1.31x faster                                               |
| xml_etree_process        | 46.5 ms                                                | 35.4 ms: 1.31x faster                                               |
| pycparser                | 877 ms                                                 | 667 ms: 1.31x faster                                                |
| coroutines               | 20.7 ms                                                | 15.9 ms: 1.30x faster                                               |
| deepcopy_reduce          | 2.33 us                                                | 1.80 us: 1.29x faster                                               |
| fannkuch                 | 303 ms                                                 | 234 ms: 1.29x faster                                                |
| sympy_sum                | 92.2 ms                                                | 71.9 ms: 1.28x faster                                               |
| scimark_sor              | 128 ms                                                 | 100 ms: 1.28x faster                                                |
| tornado_http             | 86.7 ms                                                | 68.0 ms: 1.28x faster                                               |
| django_template          | 26.4 ms                                                | 21.0 ms: 1.25x faster                                               |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                              |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                |
| sympy_integrate          | 13.1 ms                                                | 10.8 ms: 1.21x faster                                               |
| sympy_str                | 165 ms                                                 | 136 ms: 1.21x faster                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.91 ms: 1.18x faster                                               |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                |
| docutils                 | 1.73 sec                                               | 1.52 sec: 1.14x faster                                              |
| sympy_expand             | 269 ms                                                 | 235 ms: 1.14x faster                                                |
| dask                     | 253 ms                                                 | 222 ms: 1.14x faster                                                |
| sqlglot_optimize         | 36.8 ms                                                | 32.7 ms: 1.12x faster                                               |
| 2to3                     | 192 ms                                                 | 171 ms: 1.12x faster                                                |
| nqueens                  | 63.8 ms                                                | 57.2 ms: 1.11x faster                                               |
| pathlib                  | 24.5 ms                                                | 22.2 ms: 1.10x faster                                               |
| bench_thread_pool        | 527 us                                                 | 483 us: 1.09x faster                                                |
| meteor_contest           | 77.7 ms                                                | 71.5 ms: 1.09x faster                                               |
| mdp                      | 1.63 sec                                               | 1.51 sec: 1.08x faster                                              |
| genshi_text              | 17.3 ms                                                | 16.1 ms: 1.07x faster                                               |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                               |
| xml_etree_generate       | 53.5 ms                                                | 51.1 ms: 1.05x faster                                               |
| xml_etree_parse          | 108 ms                                                 | 103 ms: 1.04x faster                                                |
| xml_etree_iterparse      | 72.1 ms                                                | 70.1 ms: 1.03x faster                                               |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.02x slower                                               |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                               |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.04x slower                                               |
| regex_effbot             | 2.46 ms                                                | 2.57 ms: 1.05x slower                                               |
| unpickle_list            | 2.69 us                                                | 2.83 us: 1.05x slower                                               |
| unpickle                 | 8.80 us                                                | 9.32 us: 1.06x slower                                               |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                               |
| sqlite_synth             | 1.46 us                                                | 1.56 us: 1.07x slower                                               |
| create_gc_cycles         | 860 us                                                 | 919 us: 1.07x slower                                                |
| pickle                   | 6.97 us                                                | 7.46 us: 1.07x slower                                               |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                               |
| coverage                 | 41.5 ms                                                | 45.3 ms: 1.09x slower                                               |
| genshi_xml               | 33.8 ms                                                | 39.5 ms: 1.17x slower                                               |
| async_generators         | 231 ms                                                 | 295 ms: 1.27x slower                                                |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.30x slower                                               |
| bench_mp_pool            | 37.4 ms                                                | 49.6 ms: 1.33x slower                                               |
| flaskblogging            | 2.65 ms                                                | 3.53 ms: 1.33x slower                                               |
| python_startup           | 10.9 ms                                                | 15.7 ms: 1.44x slower                                               |
| python_startup_no_site   | 7.91 ms                                                | 13.2 ms: 1.67x slower                                               |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (12) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-darwin-arm64-brandtbucher-justin_align-3.14.0a0-0081bcd.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 0.80x