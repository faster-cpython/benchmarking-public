# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.190x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 0.49x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 172 ms: 1.11x faster                                       |
| chameleon      | 6.26 ms                                                | 4.77 ms: 1.31x faster                                      |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.19x faster                                     |
| html5lib       | 42.4 ms                                                | 35.9 ms: 1.18x faster                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 256 ms: 1.52x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 334 ms: 1.42x faster                                       |
| async_tree_io           | 980 ms                                                 | 710 ms: 1.38x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 525 ms: 1.24x faster                                       |
| Geometric mean          | (ref)                                                  | 1.39x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 71.8 ms: 1.30x faster                                      |
| float          | 69.0 ms                                                | 56.3 ms: 1.23x faster                                      |
| Geometric mean | (ref)                                                  | 1.17x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.6 ms: 1.28x faster                                      |
| regex_dna      | 174 ms                                                 | 152 ms: 1.14x faster                                       |
| regex_v8       | 17.1 ms                                                | 17.0 ms: 1.01x faster                                      |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 198 us: 1.42x faster                                       |
| unpickle_pure_python | 194 us                                                 | 155 us: 1.26x faster                                       |
| json_dumps           | 8.11 ms                                                | 6.57 ms: 1.23x faster                                      |
| xml_etree_process    | 46.5 ms                                                | 39.2 ms: 1.19x faster                                      |
| tomli_loads          | 1.71 sec                                               | 1.54 sec: 1.11x faster                                     |
| json_loads           | 16.4 us                                                | 16.8 us: 1.02x slower                                      |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                       |
| unpickle             | 8.80 us                                                | 9.01 us: 1.02x slower                                      |
| xml_etree_generate   | 53.5 ms                                                | 55.8 ms: 1.04x slower                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 75.9 ms: 1.05x slower                                      |
| pickle               | 6.97 us                                                | 7.36 us: 1.06x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.0 us: 1.06x slower                                      |
| pickle_list          | 2.74 us                                                | 2.92 us: 1.07x slower                                      |
| unpickle_list        | 2.69 us                                                | 2.99 us: 1.11x slower                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.5 ms: 1.51x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 14.7 ms: 1.86x slower                                      |
| Geometric mean         | (ref)                                                  | 1.68x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.33 ms: 1.35x faster                                      |
| django_template | 26.4 ms                                                | 21.4 ms: 1.23x faster                                      |
| genshi_text     | 17.3 ms                                                | 15.7 ms: 1.11x faster                                      |
| genshi_xml      | 33.8 ms                                                | 33.1 ms: 1.02x faster                                      |
| Geometric mean  | (ref)                                                  | 1.17x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 73.5 us: 4.39x faster                                      |
| deltablue                | 4.91 ms                                                | 2.45 ms: 2.01x faster                                      |
| raytrace                 | 301 ms                                                 | 179 ms: 1.68x faster                                       |
| asyncio_tcp              | 659 ms                                                 | 399 ms: 1.65x faster                                       |
| logging_silent           | 117 ns                                                 | 71.1 ns: 1.65x faster                                      |
| pylint                   | 277 ms                                                 | 172 ms: 1.61x faster                                       |
| chaos                    | 65.8 ms                                                | 41.3 ms: 1.59x faster                                      |
| sqlglot_parse            | 1.24 ms                                                | 807 us: 1.54x faster                                       |
| async_tree_none          | 388 ms                                                 | 256 ms: 1.52x faster                                       |
| richards_super           | 57.8 ms                                                | 38.3 ms: 1.51x faster                                      |
| comprehensions           | 16.9 us                                                | 11.2 us: 1.51x faster                                      |
| crypto_pyaes             | 71.8 ms                                                | 48.0 ms: 1.50x faster                                      |
| sqlglot_transpile        | 1.44 ms                                                | 983 us: 1.47x faster                                       |
| go                       | 151 ms                                                 | 105 ms: 1.44x faster                                       |
| async_tree_memoization   | 474 ms                                                 | 334 ms: 1.42x faster                                       |
| richards                 | 48.7 ms                                                | 34.4 ms: 1.42x faster                                      |
| pickle_pure_python       | 281 us                                                 | 198 us: 1.42x faster                                       |
| unpack_sequence          | 39.0 ns                                                | 27.6 ns: 1.41x faster                                      |
| scimark_lu               | 103 ms                                                 | 73.0 ms: 1.41x faster                                      |
| scimark_monte_carlo      | 65.6 ms                                                | 46.7 ms: 1.40x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 24.9 us: 1.39x faster                                      |
| async_tree_io            | 980 ms                                                 | 710 ms: 1.38x faster                                       |
| mako                     | 9.87 ms                                                | 7.33 ms: 1.35x faster                                      |
| chameleon                | 6.26 ms                                                | 4.77 ms: 1.31x faster                                      |
| hexiom                   | 6.19 ms                                                | 4.77 ms: 1.30x faster                                      |
| nbody                    | 93.0 ms                                                | 71.8 ms: 1.30x faster                                      |
| pprint_pformat           | 1.30 sec                                               | 1.01 sec: 1.29x faster                                     |
| pprint_safe_repr         | 641 ms                                                 | 496 ms: 1.29x faster                                       |
| sympy_sum                | 92.2 ms                                                | 71.6 ms: 1.29x faster                                      |
| spectral_norm            | 94.8 ms                                                | 74.1 ms: 1.28x faster                                      |
| regex_compile            | 95.3 ms                                                | 74.6 ms: 1.28x faster                                      |
| pyflate                  | 427 ms                                                 | 335 ms: 1.27x faster                                       |
| pycparser                | 877 ms                                                 | 693 ms: 1.27x faster                                       |
| logging_format           | 4.83 us                                                | 3.83 us: 1.26x faster                                      |
| unpickle_pure_python     | 194 us                                                 | 155 us: 1.26x faster                                       |
| logging_simple           | 4.45 us                                                | 3.55 us: 1.25x faster                                      |
| thrift                   | 572 us                                                 | 459 us: 1.25x faster                                       |
| sympy_integrate          | 13.1 ms                                                | 10.6 ms: 1.24x faster                                      |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 525 ms: 1.24x faster                                       |
| scimark_sor              | 128 ms                                                 | 104 ms: 1.23x faster                                       |
| json_dumps               | 8.11 ms                                                | 6.57 ms: 1.23x faster                                      |
| deepcopy                 | 272 us                                                 | 221 us: 1.23x faster                                       |
| django_template          | 26.4 ms                                                | 21.4 ms: 1.23x faster                                      |
| float                    | 69.0 ms                                                | 56.3 ms: 1.23x faster                                      |
| create_gc_cycles         | 860 us                                                 | 704 us: 1.22x faster                                       |
| dulwich_log              | 35.3 ms                                                | 29.1 ms: 1.22x faster                                      |
| sympy_str                | 165 ms                                                 | 137 ms: 1.21x faster                                       |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.33 sec: 1.21x faster                                     |
| deepcopy_reduce          | 2.33 us                                                | 1.93 us: 1.21x faster                                      |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.19x faster                                     |
| xml_etree_process        | 46.5 ms                                                | 39.2 ms: 1.19x faster                                      |
| html5lib                 | 42.4 ms                                                | 35.9 ms: 1.18x faster                                      |
| generators               | 32.3 ms                                                | 27.7 ms: 1.17x faster                                      |
| mypy2                    | 607 ms                                                 | 523 ms: 1.16x faster                                       |
| sympy_expand             | 269 ms                                                 | 233 ms: 1.15x faster                                       |
| regex_dna                | 174 ms                                                 | 152 ms: 1.14x faster                                       |
| coroutines               | 20.7 ms                                                | 18.3 ms: 1.13x faster                                      |
| scimark_fft              | 224 ms                                                 | 201 ms: 1.12x faster                                       |
| fannkuch                 | 303 ms                                                 | 271 ms: 1.12x faster                                       |
| 2to3                     | 192 ms                                                 | 172 ms: 1.11x faster                                       |
| tomli_loads              | 1.71 sec                                               | 1.54 sec: 1.11x faster                                     |
| genshi_text              | 17.3 ms                                                | 15.7 ms: 1.11x faster                                      |
| nqueens                  | 63.8 ms                                                | 57.8 ms: 1.10x faster                                      |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.10 ms: 1.10x faster                                      |
| sqlglot_optimize         | 36.8 ms                                                | 33.3 ms: 1.10x faster                                      |
| bench_thread_pool        | 527 us                                                 | 487 us: 1.08x faster                                       |
| meteor_contest           | 77.7 ms                                                | 72.9 ms: 1.07x faster                                      |
| sqlglot_normalize        | 190 ms                                                 | 180 ms: 1.06x faster                                       |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.04x faster                                     |
| json                     | 3.08 ms                                                | 2.99 ms: 1.03x faster                                      |
| genshi_xml               | 33.8 ms                                                | 33.1 ms: 1.02x faster                                      |
| regex_v8                 | 17.1 ms                                                | 17.0 ms: 1.01x faster                                      |
| gc_traversal             | 2.36 ms                                                | 2.41 ms: 1.02x slower                                      |
| json_loads               | 16.4 us                                                | 16.8 us: 1.02x slower                                      |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                       |
| unpickle                 | 8.80 us                                                | 9.01 us: 1.02x slower                                      |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                      |
| xml_etree_generate       | 53.5 ms                                                | 55.8 ms: 1.04x slower                                      |
| pathlib                  | 24.5 ms                                                | 25.7 ms: 1.05x slower                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 75.9 ms: 1.05x slower                                      |
| pickle                   | 6.97 us                                                | 7.36 us: 1.06x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.0 us: 1.06x slower                                      |
| pickle_list              | 2.74 us                                                | 2.92 us: 1.07x slower                                      |
| aiohttp                  | 1.22 ms                                                | 1.31 ms: 1.07x slower                                      |
| unpickle_list            | 2.69 us                                                | 2.99 us: 1.11x slower                                      |
| coverage                 | 41.5 ms                                                | 47.0 ms: 1.13x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.69 us: 1.16x slower                                      |
| telco                    | 3.49 ms                                                | 4.42 ms: 1.27x slower                                      |
| async_generators         | 231 ms                                                 | 295 ms: 1.28x slower                                       |
| bench_mp_pool            | 37.4 ms                                                | 48.5 ms: 1.30x slower                                      |
| python_startup           | 10.9 ms                                                | 16.5 ms: 1.51x slower                                      |
| flaskblogging            | 2.65 ms                                                | 4.13 ms: 1.56x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 14.7 ms: 1.86x slower                                      |
| Geometric mean           | (ref)                                                  | 1.17x faster                                               |

Benchmark hidden because not significant (4): asyncio_websockets, pidigits, gunicorn, tornado_http
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.190x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 0.49x