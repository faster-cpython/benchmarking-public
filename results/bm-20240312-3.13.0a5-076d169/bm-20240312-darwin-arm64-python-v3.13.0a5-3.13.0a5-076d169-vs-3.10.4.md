# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a5
- machine: darwin-arm64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 0.48x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 173 ms: 1.11x faster                                       |
| chameleon      | 6.26 ms                                                | 5.13 ms: 1.22x faster                                      |
| docutils       | 1.73 sec                                               | 1.47 sec: 1.18x faster                                     |
| html5lib       | 42.4 ms                                                | 35.5 ms: 1.19x faster                                      |
| tornado_http   | 86.7 ms                                                | 68.9 ms: 1.26x faster                                      |
| Geometric mean | (ref)                                                  | 1.19x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 257 ms: 1.51x faster                                       |
| async_tree_memoization  | 474 ms                                                 | 335 ms: 1.41x faster                                       |
| async_tree_io           | 980 ms                                                 | 710 ms: 1.38x faster                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 525 ms: 1.24x faster                                       |
| Geometric mean          | (ref)                                                  | 1.38x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 73.7 ms: 1.26x faster                                      |
| float          | 69.0 ms                                                | 57.0 ms: 1.21x faster                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 75.1 ms: 1.27x faster                                      |
| regex_dna      | 174 ms                                                 | 152 ms: 1.15x faster                                       |
| regex_v8       | 17.1 ms                                                | 17.1 ms: 1.00x faster                                      |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 201 us: 1.40x faster                                       |
| json_dumps           | 8.11 ms                                                | 6.52 ms: 1.24x faster                                      |
| unpickle_pure_python | 194 us                                                 | 157 us: 1.24x faster                                       |
| xml_etree_process    | 46.5 ms                                                | 40.4 ms: 1.15x faster                                      |
| tomli_loads          | 1.71 sec                                               | 1.55 sec: 1.10x faster                                     |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.01x faster                                       |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                      |
| pickle               | 6.97 us                                                | 7.31 us: 1.05x slower                                      |
| xml_etree_iterparse  | 72.1 ms                                                | 75.9 ms: 1.05x slower                                      |
| unpickle             | 8.80 us                                                | 9.30 us: 1.06x slower                                      |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| pickle_list          | 2.74 us                                                | 2.96 us: 1.08x slower                                      |
| xml_etree_generate   | 53.5 ms                                                | 58.1 ms: 1.09x slower                                      |
| unpickle_list        | 2.69 us                                                | 3.05 us: 1.13x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 12.9 ms: 1.19x slower                                      |
| python_startup_no_site | 7.91 ms                                                | 11.3 ms: 1.43x slower                                      |
| Geometric mean         | (ref)                                                  | 1.30x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.57 ms: 1.30x faster                                      |
| django_template | 26.4 ms                                                | 22.2 ms: 1.19x faster                                      |
| genshi_text     | 17.3 ms                                                | 15.9 ms: 1.09x faster                                      |
| Geometric mean  | (ref)                                                  | 1.14x faster                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 72.9 us: 4.43x faster                                      |
| deltablue                | 4.91 ms                                                | 2.45 ms: 2.00x faster                                      |
| raytrace                 | 301 ms                                                 | 171 ms: 1.76x faster                                       |
| logging_silent           | 117 ns                                                 | 70.0 ns: 1.67x faster                                      |
| chaos                    | 65.8 ms                                                | 39.9 ms: 1.65x faster                                      |
| pylint                   | 277 ms                                                 | 171 ms: 1.61x faster                                       |
| sqlglot_parse            | 1.24 ms                                                | 795 us: 1.56x faster                                       |
| richards_super           | 57.8 ms                                                | 38.0 ms: 1.52x faster                                      |
| async_tree_none          | 388 ms                                                 | 257 ms: 1.51x faster                                       |
| asyncio_tcp              | 659 ms                                                 | 438 ms: 1.50x faster                                       |
| sqlglot_transpile        | 1.44 ms                                                | 972 us: 1.48x faster                                       |
| crypto_pyaes             | 71.8 ms                                                | 48.7 ms: 1.48x faster                                      |
| go                       | 151 ms                                                 | 105 ms: 1.43x faster                                       |
| async_tree_memoization   | 474 ms                                                 | 335 ms: 1.41x faster                                       |
| richards                 | 48.7 ms                                                | 34.5 ms: 1.41x faster                                      |
| comprehensions           | 16.9 us                                                | 12.1 us: 1.40x faster                                      |
| pickle_pure_python       | 281 us                                                 | 201 us: 1.40x faster                                       |
| scimark_lu               | 103 ms                                                 | 74.3 ms: 1.38x faster                                      |
| async_tree_io            | 980 ms                                                 | 710 ms: 1.38x faster                                       |
| scimark_monte_carlo      | 65.6 ms                                                | 48.3 ms: 1.36x faster                                      |
| deepcopy_memo            | 34.7 us                                                | 25.9 us: 1.34x faster                                      |
| mypy2                    | 607 ms                                                 | 457 ms: 1.33x faster                                       |
| mako                     | 9.87 ms                                                | 7.57 ms: 1.30x faster                                      |
| hexiom                   | 6.19 ms                                                | 4.83 ms: 1.28x faster                                      |
| logging_format           | 4.83 us                                                | 3.80 us: 1.27x faster                                      |
| logging_simple           | 4.45 us                                                | 3.50 us: 1.27x faster                                      |
| regex_compile            | 95.3 ms                                                | 75.1 ms: 1.27x faster                                      |
| thrift                   | 572 us                                                 | 452 us: 1.26x faster                                       |
| nbody                    | 93.0 ms                                                | 73.7 ms: 1.26x faster                                      |
| tornado_http             | 86.7 ms                                                | 68.9 ms: 1.26x faster                                      |
| pycparser                | 877 ms                                                 | 700 ms: 1.25x faster                                       |
| spectral_norm            | 94.8 ms                                                | 75.8 ms: 1.25x faster                                      |
| pyflate                  | 427 ms                                                 | 342 ms: 1.25x faster                                       |
| json_dumps               | 8.11 ms                                                | 6.52 ms: 1.24x faster                                      |
| unpickle_pure_python     | 194 us                                                 | 157 us: 1.24x faster                                       |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 525 ms: 1.24x faster                                       |
| pprint_pformat           | 1.30 sec                                               | 1.06 sec: 1.23x faster                                     |
| sympy_sum                | 92.2 ms                                                | 75.0 ms: 1.23x faster                                      |
| pprint_safe_repr         | 641 ms                                                 | 522 ms: 1.23x faster                                       |
| chameleon                | 6.26 ms                                                | 5.13 ms: 1.22x faster                                      |
| scimark_sor              | 128 ms                                                 | 105 ms: 1.22x faster                                       |
| create_gc_cycles         | 860 us                                                 | 710 us: 1.21x faster                                       |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.32 sec: 1.21x faster                                     |
| float                    | 69.0 ms                                                | 57.0 ms: 1.21x faster                                      |
| gunicorn                 | 1.30 ms                                                | 1.08 ms: 1.20x faster                                      |
| sympy_integrate          | 13.1 ms                                                | 10.9 ms: 1.20x faster                                      |
| dulwich_log              | 35.3 ms                                                | 29.6 ms: 1.20x faster                                      |
| html5lib                 | 42.4 ms                                                | 35.5 ms: 1.19x faster                                      |
| django_template          | 26.4 ms                                                | 22.2 ms: 1.19x faster                                      |
| deepcopy                 | 272 us                                                 | 230 us: 1.18x faster                                       |
| docutils                 | 1.73 sec                                               | 1.47 sec: 1.18x faster                                     |
| aiohttp                  | 1.22 ms                                                | 1.06 ms: 1.16x faster                                      |
| sympy_str                | 165 ms                                                 | 143 ms: 1.15x faster                                       |
| xml_etree_process        | 46.5 ms                                                | 40.4 ms: 1.15x faster                                      |
| regex_dna                | 174 ms                                                 | 152 ms: 1.15x faster                                       |
| deepcopy_reduce          | 2.33 us                                                | 2.06 us: 1.13x faster                                      |
| generators               | 32.3 ms                                                | 28.6 ms: 1.13x faster                                      |
| dask                     | 253 ms                                                 | 225 ms: 1.12x faster                                       |
| 2to3                     | 192 ms                                                 | 173 ms: 1.11x faster                                       |
| sympy_expand             | 269 ms                                                 | 243 ms: 1.10x faster                                       |
| fannkuch                 | 303 ms                                                 | 274 ms: 1.10x faster                                       |
| tomli_loads              | 1.71 sec                                               | 1.55 sec: 1.10x faster                                     |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.13 ms: 1.09x faster                                      |
| genshi_text              | 17.3 ms                                                | 15.9 ms: 1.09x faster                                      |
| scimark_fft              | 224 ms                                                 | 207 ms: 1.09x faster                                       |
| coroutines               | 20.7 ms                                                | 19.2 ms: 1.08x faster                                      |
| sqlglot_optimize         | 36.8 ms                                                | 34.2 ms: 1.08x faster                                      |
| bench_thread_pool        | 527 us                                                 | 495 us: 1.07x faster                                       |
| meteor_contest           | 77.7 ms                                                | 73.6 ms: 1.06x faster                                      |
| json                     | 3.08 ms                                                | 2.95 ms: 1.04x faster                                      |
| sqlglot_normalize        | 190 ms                                                 | 185 ms: 1.03x faster                                       |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.01x faster                                       |
| regex_v8                 | 17.1 ms                                                | 17.1 ms: 1.00x faster                                      |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                       |
| mdp                      | 1.63 sec                                               | 1.64 sec: 1.01x slower                                     |
| pathlib                  | 24.5 ms                                                | 24.8 ms: 1.01x slower                                      |
| nqueens                  | 63.8 ms                                                | 65.2 ms: 1.02x slower                                      |
| gc_traversal             | 2.36 ms                                                | 2.42 ms: 1.02x slower                                      |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                      |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                      |
| pickle                   | 6.97 us                                                | 7.31 us: 1.05x slower                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 75.9 ms: 1.05x slower                                      |
| unpickle                 | 8.80 us                                                | 9.30 us: 1.06x slower                                      |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                      |
| sqlite_synth             | 1.46 us                                                | 1.57 us: 1.08x slower                                      |
| pickle_list              | 2.74 us                                                | 2.96 us: 1.08x slower                                      |
| xml_etree_generate       | 53.5 ms                                                | 58.1 ms: 1.09x slower                                      |
| unpickle_list            | 2.69 us                                                | 3.05 us: 1.13x slower                                      |
| coverage                 | 41.5 ms                                                | 48.4 ms: 1.17x slower                                      |
| python_startup           | 10.9 ms                                                | 12.9 ms: 1.19x slower                                      |
| bench_mp_pool            | 37.4 ms                                                | 45.4 ms: 1.22x slower                                      |
| flaskblogging            | 2.65 ms                                                | 3.40 ms: 1.28x slower                                      |
| async_generators         | 231 ms                                                 | 302 ms: 1.31x slower                                       |
| telco                    | 3.49 ms                                                | 4.63 ms: 1.33x slower                                      |
| python_startup_no_site   | 7.91 ms                                                | 11.3 ms: 1.43x slower                                      |
| Geometric mean           | (ref)                                                  | 1.17x faster                                               |

Benchmark hidden because not significant (2): genshi_xml, pidigits
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (12) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-darwin-arm64-python-v3.13.0a5-3.13.0a5-076d169.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 0.48x