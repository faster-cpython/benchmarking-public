# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: darwin-arm64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 0.58x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 162 ms: 1.18x faster                                         |
| docutils       | 1.73 sec                                               | 1.43 sec: 1.21x faster                                       |
| html5lib       | 42.4 ms                                                | 30.2 ms: 1.40x faster                                        |
| Geometric mean | (ref)                                                  | 1.21x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 200 ms: 1.94x faster                                         |
| async_tree_memoization  | 474 ms                                                 | 247 ms: 1.92x faster                                         |
| async_tree_io           | 980 ms                                                 | 583 ms: 1.68x faster                                         |
| async_tree_cpu_io_mixed | 649 ms                                                 | 460 ms: 1.41x faster                                         |
| Geometric mean          | (ref)                                                  | 1.72x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.6 ms: 1.56x faster                                        |
| float          | 69.0 ms                                                | 48.9 ms: 1.41x faster                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.4 ms: 1.41x faster                                        |
| regex_dna      | 174 ms                                                 | 145 ms: 1.21x faster                                         |
| regex_v8       | 17.1 ms                                                | 16.4 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                  | 1.15x faster                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 184 us: 1.52x faster                                         |
| unpickle_pure_python | 194 us                                                 | 140 us: 1.39x faster                                         |
| json_dumps           | 8.11 ms                                                | 6.46 ms: 1.25x faster                                        |
| xml_etree_process    | 46.5 ms                                                | 37.6 ms: 1.24x faster                                        |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.15x faster                                       |
| xml_etree_iterparse  | 72.1 ms                                                | 73.6 ms: 1.02x slower                                        |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                        |
| pickle               | 6.97 us                                                | 7.40 us: 1.06x slower                                        |
| unpickle             | 8.80 us                                                | 9.43 us: 1.07x slower                                        |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                        |
| unpickle_list        | 2.69 us                                                | 2.92 us: 1.09x slower                                        |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                 |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.5 ms: 1.52x slower                                        |
| python_startup_no_site | 7.91 ms                                                | 13.6 ms: 1.71x slower                                        |
| Geometric mean         | (ref)                                                  | 1.61x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.97 ms: 1.42x faster                                        |
| django_template | 26.4 ms                                                | 19.8 ms: 1.33x faster                                        |
| genshi_text     | 17.3 ms                                                | 13.9 ms: 1.24x faster                                        |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.12x faster                                        |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 90.4 us: 3.57x faster                                        |
| deltablue                | 4.91 ms                                                | 2.14 ms: 2.30x faster                                        |
| deepcopy_memo            | 34.7 us                                                | 16.4 us: 2.11x faster                                        |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                         |
| async_tree_none          | 388 ms                                                 | 200 ms: 1.94x faster                                         |
| logging_silent           | 117 ns                                                 | 60.6 ns: 1.93x faster                                        |
| async_tree_memoization   | 474 ms                                                 | 247 ms: 1.92x faster                                         |
| go                       | 151 ms                                                 | 79.3 ms: 1.90x faster                                        |
| deepcopy                 | 272 us                                                 | 144 us: 1.89x faster                                         |
| chaos                    | 65.8 ms                                                | 35.7 ms: 1.84x faster                                        |
| async_tree_io            | 980 ms                                                 | 583 ms: 1.68x faster                                         |
| sqlglot_parse            | 1.24 ms                                                | 741 us: 1.68x faster                                         |
| comprehensions           | 16.9 us                                                | 10.1 us: 1.68x faster                                        |
| richards_super           | 57.8 ms                                                | 36.0 ms: 1.60x faster                                        |
| sqlglot_transpile        | 1.44 ms                                                | 908 us: 1.59x faster                                         |
| asyncio_tcp              | 659 ms                                                 | 422 ms: 1.56x faster                                         |
| nbody                    | 93.0 ms                                                | 59.6 ms: 1.56x faster                                        |
| generators               | 32.3 ms                                                | 20.8 ms: 1.56x faster                                        |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.55x faster                                        |
| scimark_lu               | 103 ms                                                 | 67.0 ms: 1.54x faster                                        |
| pylint                   | 277 ms                                                 | 181 ms: 1.53x faster                                         |
| hexiom                   | 6.19 ms                                                | 4.05 ms: 1.53x faster                                        |
| pickle_pure_python       | 281 us                                                 | 184 us: 1.52x faster                                         |
| scimark_monte_carlo      | 65.6 ms                                                | 43.1 ms: 1.52x faster                                        |
| richards                 | 48.7 ms                                                | 32.3 ms: 1.51x faster                                        |
| unpack_sequence          | 39.0 ns                                                | 26.5 ns: 1.47x faster                                        |
| logging_simple           | 4.45 us                                                | 3.03 us: 1.47x faster                                        |
| logging_format           | 4.83 us                                                | 3.32 us: 1.45x faster                                        |
| crypto_pyaes             | 71.8 ms                                                | 50.3 ms: 1.43x faster                                        |
| mako                     | 9.87 ms                                                | 6.97 ms: 1.42x faster                                        |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 460 ms: 1.41x faster                                         |
| regex_compile            | 95.3 ms                                                | 67.4 ms: 1.41x faster                                        |
| float                    | 69.0 ms                                                | 48.9 ms: 1.41x faster                                        |
| spectral_norm            | 94.8 ms                                                | 67.5 ms: 1.40x faster                                        |
| pprint_safe_repr         | 641 ms                                                 | 456 ms: 1.40x faster                                         |
| html5lib                 | 42.4 ms                                                | 30.2 ms: 1.40x faster                                        |
| pprint_pformat           | 1.30 sec                                               | 932 ms: 1.40x faster                                         |
| unpickle_pure_python     | 194 us                                                 | 140 us: 1.39x faster                                         |
| pycparser                | 877 ms                                                 | 638 ms: 1.37x faster                                         |
| scimark_sor              | 128 ms                                                 | 93.5 ms: 1.37x faster                                        |
| thrift                   | 572 us                                                 | 425 us: 1.35x faster                                         |
| sympy_sum                | 92.2 ms                                                | 69.0 ms: 1.34x faster                                        |
| django_template          | 26.4 ms                                                | 19.8 ms: 1.33x faster                                        |
| pyflate                  | 427 ms                                                 | 322 ms: 1.33x faster                                         |
| dulwich_log              | 35.3 ms                                                | 27.3 ms: 1.29x faster                                        |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                        |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                        |
| json_dumps               | 8.11 ms                                                | 6.46 ms: 1.25x faster                                        |
| sympy_str                | 165 ms                                                 | 132 ms: 1.25x faster                                         |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                       |
| genshi_text              | 17.3 ms                                                | 13.9 ms: 1.24x faster                                        |
| xml_etree_process        | 46.5 ms                                                | 37.6 ms: 1.24x faster                                        |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                         |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.81 ms: 1.22x faster                                        |
| docutils                 | 1.73 sec                                               | 1.43 sec: 1.21x faster                                       |
| regex_dna                | 174 ms                                                 | 145 ms: 1.21x faster                                         |
| nqueens                  | 63.8 ms                                                | 53.6 ms: 1.19x faster                                        |
| 2to3                     | 192 ms                                                 | 162 ms: 1.18x faster                                         |
| sympy_expand             | 269 ms                                                 | 228 ms: 1.18x faster                                         |
| sqlglot_optimize         | 36.8 ms                                                | 31.3 ms: 1.17x faster                                        |
| bench_thread_pool        | 527 us                                                 | 450 us: 1.17x faster                                         |
| fannkuch                 | 303 ms                                                 | 260 ms: 1.16x faster                                         |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.15x faster                                       |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                       |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                         |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.12x faster                                        |
| meteor_contest           | 77.7 ms                                                | 71.6 ms: 1.09x faster                                        |
| regex_v8                 | 17.1 ms                                                | 16.4 ms: 1.04x faster                                        |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                        |
| json                     | 3.08 ms                                                | 2.97 ms: 1.04x faster                                        |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                         |
| xml_etree_iterparse      | 72.1 ms                                                | 73.6 ms: 1.02x slower                                        |
| create_gc_cycles         | 860 us                                                 | 888 us: 1.03x slower                                         |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                        |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                        |
| pickle                   | 6.97 us                                                | 7.40 us: 1.06x slower                                        |
| sqlite_synth             | 1.46 us                                                | 1.56 us: 1.07x slower                                        |
| unpickle                 | 8.80 us                                                | 9.43 us: 1.07x slower                                        |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                        |
| coverage                 | 41.5 ms                                                | 44.9 ms: 1.08x slower                                        |
| unpickle_list            | 2.69 us                                                | 2.92 us: 1.09x slower                                        |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                        |
| async_generators         | 231 ms                                                 | 282 ms: 1.22x slower                                         |
| bench_mp_pool            | 37.4 ms                                                | 48.5 ms: 1.30x slower                                        |
| telco                    | 3.49 ms                                                | 4.87 ms: 1.40x slower                                        |
| python_startup           | 10.9 ms                                                | 16.5 ms: 1.52x slower                                        |
| python_startup_no_site   | 7.91 ms                                                | 13.6 ms: 1.71x slower                                        |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                 |

Benchmark hidden because not significant (5): tornado_http, pidigits, xml_etree_generate, regex_effbot, xml_etree_parse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-darwin-arm64-brandtbucher-nojit-3.14.0a0-a6f1035.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 0.58x