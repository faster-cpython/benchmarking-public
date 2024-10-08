# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| chameleon      | 6.26 ms                                                | 4.73 ms: 1.32x faster                                      |
| docutils       | 1.73 sec                                               | 1.46 sec: 1.19x faster                                     |
| html5lib       | 42.4 ms                                                | 36.0 ms: 1.18x faster                                      |
| tornado_http   | 86.7 ms                                                | 76.9 ms: 1.13x faster                                      |
| Geometric mean | (ref)                                                  | 1.16x faster                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 255 ms: 1.53x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 331 ms: 1.43x faster                                       |
| async_tree_io           | 980 ms                                                 | 706 ms: 1.39x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 522 ms: 1.24x faster                                       |
| Geometric mean          | (ref)                                                  | 1.39x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 70.8 ms: 1.31x faster                                      |
| float          | 69.0 ms                                                | 56.4 ms: 1.22x faster                                      |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.17x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.9 ms: 1.27x faster                                      |
| regex_dna      | 174 ms                                                 | 152 ms: 1.15x faster                                       |
| regex_v8       | 17.1 ms                                                | 17.1 ms: 1.01x faster                                      |
| regex_effbot   | 2.46 ms                                                | 2.57 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 198 us: 1.42x faster                                       |
| unpickle_pure_python | 194 us                                                 | 155 us: 1.25x faster                                       |
| json_dumps           | 8.11 ms                                                | 6.61 ms: 1.23x faster                                      |
| xml_etree_process    | 46.5 ms                                                | 39.5 ms: 1.18x faster                                      |
| tomli_loads          | 1.71 sec                                               | 1.53 sec: 1.11x faster                                     |
| xml_etree_parse      | 108 ms                                                 | 99.9 ms: 1.08x faster                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 71.3 ms: 1.01x faster                                      |
| unpickle             | 8.80 us                                                | 9.10 us: 1.03x slower                                      |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                      |
| xml_etree_generate   | 53.5 ms                                                | 56.2 ms: 1.05x slower                                      |
| pickle               | 6.97 us                                                | 7.39 us: 1.06x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.06x slower                                      |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                      |
| unpickle_list        | 2.69 us                                                | 2.98 us: 1.10x slower                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 13.9 ms: 1.28x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 12.4 ms: 1.56x slower                                      |
| Geometric mean         | (ref)                                                  | 1.41x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.39 ms: 1.34x faster                                      |
| django_template | 26.4 ms                                                | 21.5 ms: 1.23x faster                                      |
| genshi_text     | 17.3 ms                                                | 15.7 ms: 1.11x faster                                      |
| genshi_xml      | 33.8 ms                                                | 33.0 ms: 1.02x faster                                      |
| Geometric mean  | (ref)                                                  | 1.17x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 73.6 us: 4.39x faster                                      |
| deltablue                | 4.91 ms                                                | 2.44 ms: 2.02x faster                                      |
| raytrace                 | 301 ms                                                 | 178 ms: 1.69x faster                                       |
| logging_silent           | 117 ns                                                 | 69.9 ns: 1.68x faster                                      |
| pylint                   | 277 ms                                                 | 168 ms: 1.65x faster                                       |
| chaos                    | 65.8 ms                                                | 41.2 ms: 1.60x faster                                      |
| sqlglot_parse            | 1.24 ms                                                | 807 us: 1.54x faster                                       |
| async_tree_none          | 388 ms                                                 | 255 ms: 1.53x faster                                       |
| richards_super           | 57.8 ms                                                | 38.0 ms: 1.52x faster                                      |
| asyncio_tcp              | 659 ms                                                 | 436 ms: 1.51x faster                                       |
| crypto_pyaes             | 71.8 ms                                                | 48.0 ms: 1.50x faster                                      |
| comprehensions           | 16.9 us                                                | 11.4 us: 1.49x faster                                      |
| sqlglot_transpile        | 1.44 ms                                                | 980 us: 1.47x faster                                       |
| richards                 | 48.7 ms                                                | 33.9 ms: 1.44x faster                                      |
| go                       | 151 ms                                                 | 105 ms: 1.44x faster                                       |
| async_tree_memoization   | 474 ms                                                 | 331 ms: 1.43x faster                                       |
| pickle_pure_python       | 281 us                                                 | 198 us: 1.42x faster                                       |
| scimark_lu               | 103 ms                                                 | 72.7 ms: 1.41x faster                                      |
| scimark_monte_carlo      | 65.6 ms                                                | 46.6 ms: 1.41x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 24.8 us: 1.40x faster                                      |
| async_tree_io            | 980 ms                                                 | 706 ms: 1.39x faster                                       |
| mako                     | 9.87 ms                                                | 7.39 ms: 1.34x faster                                      |
| chameleon                | 6.26 ms                                                | 4.73 ms: 1.32x faster                                      |
| nbody                    | 93.0 ms                                                | 70.8 ms: 1.31x faster                                      |
| hexiom                   | 6.19 ms                                                | 4.77 ms: 1.30x faster                                      |
| pprint_pformat           | 1.30 sec                                               | 1.01 sec: 1.29x faster                                     |
| pprint_safe_repr         | 641 ms                                                 | 496 ms: 1.29x faster                                       |
| spectral_norm            | 94.8 ms                                                | 74.0 ms: 1.28x faster                                      |
| sympy_sum                | 92.2 ms                                                | 72.0 ms: 1.28x faster                                      |
| pyflate                  | 427 ms                                                 | 335 ms: 1.28x faster                                       |
| regex_compile            | 95.3 ms                                                | 74.9 ms: 1.27x faster                                      |
| pycparser                | 877 ms                                                 | 694 ms: 1.26x faster                                       |
| logging_format           | 4.83 us                                                | 3.84 us: 1.26x faster                                      |
| logging_simple           | 4.45 us                                                | 3.54 us: 1.26x faster                                      |
| unpickle_pure_python     | 194 us                                                 | 155 us: 1.25x faster                                       |
| thrift                   | 572 us                                                 | 457 us: 1.25x faster                                       |
| deepcopy                 | 272 us                                                 | 218 us: 1.25x faster                                       |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 522 ms: 1.24x faster                                       |
| sympy_integrate          | 13.1 ms                                                | 10.6 ms: 1.24x faster                                      |
| scimark_sor              | 128 ms                                                 | 104 ms: 1.23x faster                                       |
| django_template          | 26.4 ms                                                | 21.5 ms: 1.23x faster                                      |
| json_dumps               | 8.11 ms                                                | 6.61 ms: 1.23x faster                                      |
| float                    | 69.0 ms                                                | 56.4 ms: 1.22x faster                                      |
| create_gc_cycles         | 860 us                                                 | 703 us: 1.22x faster                                       |
| deepcopy_reduce          | 2.33 us                                                | 1.92 us: 1.21x faster                                      |
| dulwich_log              | 35.3 ms                                                | 29.2 ms: 1.21x faster                                      |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.32 sec: 1.21x faster                                     |
| sympy_str                | 165 ms                                                 | 137 ms: 1.21x faster                                       |
| docutils                 | 1.73 sec                                               | 1.46 sec: 1.19x faster                                     |
| html5lib                 | 42.4 ms                                                | 36.0 ms: 1.18x faster                                      |
| xml_etree_process        | 46.5 ms                                                | 39.5 ms: 1.18x faster                                      |
| generators               | 32.3 ms                                                | 28.0 ms: 1.16x faster                                      |
| sympy_expand             | 269 ms                                                 | 234 ms: 1.15x faster                                       |
| regex_dna                | 174 ms                                                 | 152 ms: 1.15x faster                                       |
| tornado_http             | 86.7 ms                                                | 76.9 ms: 1.13x faster                                      |
| scimark_fft              | 224 ms                                                 | 200 ms: 1.12x faster                                       |
| fannkuch                 | 303 ms                                                 | 270 ms: 1.12x faster                                       |
| tomli_loads              | 1.71 sec                                               | 1.53 sec: 1.11x faster                                     |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.08 ms: 1.11x faster                                      |
| genshi_text              | 17.3 ms                                                | 15.7 ms: 1.11x faster                                      |
| coroutines               | 20.7 ms                                                | 18.8 ms: 1.10x faster                                      |
| sqlglot_optimize         | 36.8 ms                                                | 33.3 ms: 1.10x faster                                      |
| nqueens                  | 63.8 ms                                                | 58.4 ms: 1.09x faster                                      |
| xml_etree_parse          | 108 ms                                                 | 99.9 ms: 1.08x faster                                      |
| bench_thread_pool        | 527 us                                                 | 493 us: 1.07x faster                                       |
| meteor_contest           | 77.7 ms                                                | 73.0 ms: 1.07x faster                                      |
| sqlglot_normalize        | 190 ms                                                 | 179 ms: 1.06x faster                                       |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.05x faster                                     |
| json                     | 3.08 ms                                                | 2.97 ms: 1.04x faster                                      |
| genshi_xml               | 33.8 ms                                                | 33.0 ms: 1.02x faster                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 71.3 ms: 1.01x faster                                      |
| regex_v8                 | 17.1 ms                                                | 17.1 ms: 1.01x faster                                      |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| gc_traversal             | 2.36 ms                                                | 2.40 ms: 1.01x slower                                      |
| aiohttp                  | 1.22 ms                                                | 1.26 ms: 1.03x slower                                      |
| unpickle                 | 8.80 us                                                | 9.10 us: 1.03x slower                                      |
| regex_effbot             | 2.46 ms                                                | 2.57 ms: 1.04x slower                                      |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                      |
| xml_etree_generate       | 53.5 ms                                                | 56.2 ms: 1.05x slower                                      |
| pickle                   | 6.97 us                                                | 7.39 us: 1.06x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.06x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.58 us: 1.09x slower                                      |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                      |
| unpickle_list            | 2.69 us                                                | 2.98 us: 1.10x slower                                      |
| coverage                 | 41.5 ms                                                | 47.1 ms: 1.13x slower                                      |
| bench_mp_pool            | 37.4 ms                                                | 44.7 ms: 1.20x slower                                      |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                       |
| python_startup           | 10.9 ms                                                | 13.9 ms: 1.28x slower                                      |
| telco                    | 3.49 ms                                                | 4.54 ms: 1.30x slower                                      |
| flaskblogging            | 2.65 ms                                                | 3.89 ms: 1.47x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 12.4 ms: 1.56x slower                                      |
| Geometric mean           | (ref)                                                  | 1.18x faster                                               |

Benchmark hidden because not significant (5): mypy2, asyncio_websockets, pathlib, 2to3, gunicorn
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (12) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.11x