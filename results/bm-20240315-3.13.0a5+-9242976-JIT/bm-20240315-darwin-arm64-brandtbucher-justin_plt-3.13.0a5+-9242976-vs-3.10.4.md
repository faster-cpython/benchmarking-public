# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_plt
- machine: darwin-arm64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.60x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 182 ms: 1.05x faster                                               |
| chameleon      | 6.26 ms                                                | 4.81 ms: 1.30x faster                                              |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.16x faster                                             |
| html5lib       | 42.4 ms                                                | 35.5 ms: 1.19x faster                                              |
| Geometric mean | (ref)                                                  | 1.14x faster                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 253 ms: 1.53x faster                                               |
| async_tree_memoization  | 474 ms                                                 | 331 ms: 1.43x faster                                               |
| async_tree_io           | 980 ms                                                 | 708 ms: 1.38x faster                                               |
| async_tree_cpu_io_mixed | 649 ms                                                 | 523 ms: 1.24x faster                                               |
| Geometric mean          | (ref)                                                  | 1.39x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 69.2 ms: 1.34x faster                                              |
| float          | 69.0 ms                                                | 52.6 ms: 1.31x faster                                              |
| Geometric mean | (ref)                                                  | 1.21x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 76.8 ms: 1.24x faster                                              |
| regex_dna      | 174 ms                                                 | 152 ms: 1.15x faster                                               |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.00x slower                                              |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 198 us: 1.42x faster                                               |
| tomli_loads          | 1.71 sec                                               | 1.29 sec: 1.33x faster                                             |
| unpickle_pure_python | 194 us                                                 | 147 us: 1.32x faster                                               |
| json_dumps           | 8.11 ms                                                | 6.51 ms: 1.25x faster                                              |
| xml_etree_process    | 46.5 ms                                                | 39.0 ms: 1.19x faster                                              |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 72.1 ms                                                | 74.3 ms: 1.03x slower                                              |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                              |
| pickle               | 6.97 us                                                | 7.25 us: 1.04x slower                                              |
| unpickle             | 8.80 us                                                | 9.17 us: 1.04x slower                                              |
| xml_etree_generate   | 53.5 ms                                                | 56.2 ms: 1.05x slower                                              |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                              |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                              |
| unpickle_list        | 2.69 us                                                | 3.08 us: 1.15x slower                                              |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.2 ms: 1.58x slower                                              |
| python_startup_no_site | 7.91 ms                                                | 15.6 ms: 1.97x slower                                              |
| Geometric mean         | (ref)                                                  | 1.76x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.55 ms: 1.51x faster                                              |
| django_template | 26.4 ms                                                | 21.9 ms: 1.20x faster                                              |
| genshi_text     | 17.3 ms                                                | 15.5 ms: 1.12x faster                                              |
| genshi_xml      | 33.8 ms                                                | 34.6 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 71.4 us: 4.52x faster                                              |
| deltablue                | 4.91 ms                                                | 2.51 ms: 1.96x faster                                              |
| chaos                    | 65.8 ms                                                | 39.5 ms: 1.67x faster                                              |
| logging_silent           | 117 ns                                                 | 72.1 ns: 1.63x faster                                              |
| raytrace                 | 301 ms                                                 | 187 ms: 1.61x faster                                               |
| pylint                   | 277 ms                                                 | 173 ms: 1.60x faster                                               |
| asyncio_tcp              | 659 ms                                                 | 412 ms: 1.60x faster                                               |
| richards_super           | 57.8 ms                                                | 36.4 ms: 1.59x faster                                              |
| scimark_monte_carlo      | 65.6 ms                                                | 42.1 ms: 1.56x faster                                              |
| sqlglot_parse            | 1.24 ms                                                | 805 us: 1.54x faster                                               |
| crypto_pyaes             | 71.8 ms                                                | 46.5 ms: 1.54x faster                                              |
| async_tree_none          | 388 ms                                                 | 253 ms: 1.53x faster                                               |
| mako                     | 9.87 ms                                                | 6.55 ms: 1.51x faster                                              |
| richards                 | 48.7 ms                                                | 32.6 ms: 1.49x faster                                              |
| sqlglot_transpile        | 1.44 ms                                                | 988 us: 1.46x faster                                               |
| async_tree_memoization   | 474 ms                                                 | 331 ms: 1.43x faster                                               |
| pickle_pure_python       | 281 us                                                 | 198 us: 1.42x faster                                               |
| go                       | 151 ms                                                 | 107 ms: 1.41x faster                                               |
| comprehensions           | 16.9 us                                                | 12.1 us: 1.40x faster                                              |
| async_tree_io            | 980 ms                                                 | 708 ms: 1.38x faster                                               |
| pprint_safe_repr         | 641 ms                                                 | 473 ms: 1.35x faster                                               |
| nbody                    | 93.0 ms                                                | 69.2 ms: 1.34x faster                                              |
| pprint_pformat           | 1.30 sec                                               | 972 ms: 1.34x faster                                               |
| pyflate                  | 427 ms                                                 | 318 ms: 1.34x faster                                               |
| deepcopy_memo            | 34.7 us                                                | 26.0 us: 1.34x faster                                              |
| hexiom                   | 6.19 ms                                                | 4.64 ms: 1.33x faster                                              |
| tomli_loads              | 1.71 sec                                               | 1.29 sec: 1.33x faster                                             |
| unpickle_pure_python     | 194 us                                                 | 147 us: 1.32x faster                                               |
| spectral_norm            | 94.8 ms                                                | 72.2 ms: 1.31x faster                                              |
| float                    | 69.0 ms                                                | 52.6 ms: 1.31x faster                                              |
| chameleon                | 6.26 ms                                                | 4.81 ms: 1.30x faster                                              |
| logging_simple           | 4.45 us                                                | 3.45 us: 1.29x faster                                              |
| logging_format           | 4.83 us                                                | 3.74 us: 1.29x faster                                              |
| json_dumps               | 8.11 ms                                                | 6.51 ms: 1.25x faster                                              |
| pycparser                | 877 ms                                                 | 705 ms: 1.24x faster                                               |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 523 ms: 1.24x faster                                               |
| regex_compile            | 95.3 ms                                                | 76.8 ms: 1.24x faster                                              |
| thrift                   | 572 us                                                 | 464 us: 1.23x faster                                               |
| sympy_sum                | 92.2 ms                                                | 75.0 ms: 1.23x faster                                              |
| scimark_lu               | 103 ms                                                 | 83.9 ms: 1.23x faster                                              |
| fannkuch                 | 303 ms                                                 | 247 ms: 1.22x faster                                               |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.22x faster                                             |
| django_template          | 26.4 ms                                                | 21.9 ms: 1.20x faster                                              |
| create_gc_cycles         | 860 us                                                 | 719 us: 1.20x faster                                               |
| xml_etree_process        | 46.5 ms                                                | 39.0 ms: 1.19x faster                                              |
| deepcopy                 | 272 us                                                 | 228 us: 1.19x faster                                               |
| html5lib                 | 42.4 ms                                                | 35.5 ms: 1.19x faster                                              |
| sympy_integrate          | 13.1 ms                                                | 11.1 ms: 1.19x faster                                              |
| deepcopy_reduce          | 2.33 us                                                | 1.97 us: 1.18x faster                                              |
| sympy_str                | 165 ms                                                 | 142 ms: 1.17x faster                                               |
| scimark_sor              | 128 ms                                                 | 110 ms: 1.17x faster                                               |
| dulwich_log              | 35.3 ms                                                | 30.5 ms: 1.16x faster                                              |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.16x faster                                             |
| scimark_fft              | 224 ms                                                 | 195 ms: 1.15x faster                                               |
| regex_dna                | 174 ms                                                 | 152 ms: 1.15x faster                                               |
| generators               | 32.3 ms                                                | 28.3 ms: 1.14x faster                                              |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.03 ms: 1.13x faster                                              |
| coroutines               | 20.7 ms                                                | 18.4 ms: 1.13x faster                                              |
| gunicorn                 | 1.30 ms                                                | 1.16 ms: 1.12x faster                                              |
| genshi_text              | 17.3 ms                                                | 15.5 ms: 1.12x faster                                              |
| aiohttp                  | 1.22 ms                                                | 1.10 ms: 1.11x faster                                              |
| dask                     | 253 ms                                                 | 229 ms: 1.10x faster                                               |
| sympy_expand             | 269 ms                                                 | 246 ms: 1.09x faster                                               |
| sqlglot_optimize         | 36.8 ms                                                | 34.5 ms: 1.07x faster                                              |
| 2to3                     | 192 ms                                                 | 182 ms: 1.05x faster                                               |
| sqlglot_normalize        | 190 ms                                                 | 181 ms: 1.05x faster                                               |
| meteor_contest           | 77.7 ms                                                | 74.1 ms: 1.05x faster                                              |
| json                     | 3.08 ms                                                | 2.95 ms: 1.04x faster                                              |
| bench_thread_pool        | 527 us                                                 | 508 us: 1.04x faster                                               |
| mdp                      | 1.63 sec                                               | 1.60 sec: 1.02x faster                                             |
| nqueens                  | 63.8 ms                                                | 63.1 ms: 1.01x faster                                              |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                               |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.00x slower                                              |
| gc_traversal             | 2.36 ms                                                | 2.41 ms: 1.02x slower                                              |
| genshi_xml               | 33.8 ms                                                | 34.6 ms: 1.02x slower                                              |
| pathlib                  | 24.5 ms                                                | 25.0 ms: 1.02x slower                                              |
| xml_etree_iterparse      | 72.1 ms                                                | 74.3 ms: 1.03x slower                                              |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                              |
| pickle                   | 6.97 us                                                | 7.25 us: 1.04x slower                                              |
| unpickle                 | 8.80 us                                                | 9.17 us: 1.04x slower                                              |
| xml_etree_generate       | 53.5 ms                                                | 56.2 ms: 1.05x slower                                              |
| regex_effbot             | 2.46 ms                                                | 2.63 ms: 1.07x slower                                              |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                              |
| sqlite_synth             | 1.46 us                                                | 1.59 us: 1.09x slower                                              |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                              |
| coverage                 | 41.5 ms                                                | 47.5 ms: 1.14x slower                                              |
| unpickle_list            | 2.69 us                                                | 3.08 us: 1.15x slower                                              |
| telco                    | 3.49 ms                                                | 4.44 ms: 1.27x slower                                              |
| async_generators         | 231 ms                                                 | 311 ms: 1.34x slower                                               |
| bench_mp_pool            | 37.4 ms                                                | 51.3 ms: 1.37x slower                                              |
| python_startup           | 10.9 ms                                                | 17.2 ms: 1.58x slower                                              |
| unpack_sequence          | 39.0 ns                                                | 72.7 ns: 1.86x slower                                              |
| python_startup_no_site   | 7.91 ms                                                | 15.6 ms: 1.97x slower                                              |
| Geometric mean           | (ref)                                                  | 1.17x faster                                                       |

Benchmark hidden because not significant (4): tornado_http, asyncio_websockets, pidigits, mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-darwin-arm64-brandtbucher-justin_plt-3.13.0a5+-9242976.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x


# Memory

- memory change: 1.60x