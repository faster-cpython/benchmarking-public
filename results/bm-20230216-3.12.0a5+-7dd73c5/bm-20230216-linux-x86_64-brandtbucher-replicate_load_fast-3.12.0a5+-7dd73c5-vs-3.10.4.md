
# Results vs. 3.10.4

- fork: brandtbucher
- ref: replicate_load_fast
- machine: linux-x86_64
- commit hash: 7dd73c5
- commit date: 2023-02-16
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 248 ms: 1.36x faster                                                        |
| chameleon      | 9.06 ms                                                | 6.34 ms: 1.43x faster                                                       |
| docutils       | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                      |
| html5lib       | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                       |
| tornado_http   | 127 ms                                                 | 95.5 ms: 1.33x faster                                                       |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.6 ms: 1.52x faster                                                       |
| nbody          | 142 ms                                                 | 93.2 ms: 1.52x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                       |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.67 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                        |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.66 ms: 1.40x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 56.5 ms: 1.33x faster                                                       |
| json_loads           | 28.8 us                                                | 24.1 us: 1.19x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 82.5 ms: 1.14x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.26 us: 1.07x faster                                                       |
| unpickle             | 14.1 us                                                | 13.5 us: 1.05x faster                                                       |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| unpickle_list        | 4.82 us                                                | 5.13 us: 1.06x slower                                                       |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.00 ms: 1.57x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.67 ms: 1.53x faster                                                       |
| genshi_text     | 30.3 ms                                                | 21.1 ms: 1.44x faster                                                       |
| django_template | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                       |
| genshi_xml      | 63.3 ms                                                | 47.4 ms: 1.34x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.6 ms: 2.51x faster                                                       |
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                                       |
| logging_silent          | 175 ns                                                 | 94.1 ns: 1.86x faster                                                       |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                        |
| asyncio_tcp             | 925 ms                                                 | 505 ms: 1.83x faster                                                        |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                                       |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                        |
| scimark_monte_carlo     | 108 ms                                                 | 65.2 ms: 1.66x faster                                                       |
| pyflate                 | 673 ms                                                 | 406 ms: 1.66x faster                                                        |
| raytrace                | 464 ms                                                 | 288 ms: 1.61x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 73.5 ms: 1.61x faster                                                       |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                        |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.60x faster                                                       |
| chaos                   | 106 ms                                                 | 67.3 ms: 1.58x faster                                                       |
| python_startup          | 14.2 ms                                                | 9.00 ms: 1.57x faster                                                       |
| unpack_sequence         | 64.7 ns                                                | 41.4 ns: 1.56x faster                                                       |
| hexiom                  | 9.53 ms                                                | 6.24 ms: 1.53x faster                                                       |
| mako                    | 14.8 ms                                                | 9.67 ms: 1.53x faster                                                       |
| float                   | 111 ms                                                 | 72.6 ms: 1.52x faster                                                       |
| nbody                   | 142 ms                                                 | 93.2 ms: 1.52x faster                                                       |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                        |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                        |
| deepcopy_memo           | 52.3 us                                                | 35.0 us: 1.49x faster                                                       |
| genshi_text             | 30.3 ms                                                | 21.1 ms: 1.44x faster                                                       |
| coroutines              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                       |
| chameleon               | 9.06 ms                                                | 6.34 ms: 1.43x faster                                                       |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                                       |
| logging_simple          | 8.07 us                                                | 5.69 us: 1.42x faster                                                       |
| logging_format          | 8.91 us                                                | 6.28 us: 1.42x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.41x faster                                                       |
| pprint_pformat          | 1.99 sec                                               | 1.41 sec: 1.41x faster                                                      |
| json_dumps              | 13.5 ms                                                | 9.66 ms: 1.40x faster                                                       |
| html5lib                | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                       |
| django_template         | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                       |
| pprint_safe_repr        | 955 ms                                                 | 692 ms: 1.38x faster                                                        |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                       |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                        |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.36x faster                                                      |
| thrift                  | 1.03 ms                                                | 760 us: 1.36x faster                                                        |
| 2to3                    | 336 ms                                                 | 248 ms: 1.36x faster                                                        |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                                       |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                        |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                       |
| genshi_xml              | 63.3 ms                                                | 47.4 ms: 1.34x faster                                                       |
| tornado_http            | 127 ms                                                 | 95.5 ms: 1.33x faster                                                       |
| xml_etree_process       | 74.9 ms                                                | 56.5 ms: 1.33x faster                                                       |
| async_tree_memoization  | 854 ms                                                 | 646 ms: 1.32x faster                                                        |
| deepcopy                | 442 us                                                 | 335 us: 1.32x faster                                                        |
| fannkuch                | 486 ms                                                 | 368 ms: 1.32x faster                                                        |
| deepcopy_reduce         | 3.82 us                                                | 2.96 us: 1.29x faster                                                       |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed | 951 ms                                                 | 740 ms: 1.28x faster                                                        |
| mypy2                   | 428 ms                                                 | 335 ms: 1.28x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                                       |
| nqueens                 | 100 ms                                                 | 79.5 ms: 1.26x faster                                                       |
| docutils                | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                      |
| sympy_integrate         | 24.3 ms                                                | 20.0 ms: 1.22x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                        |
| bench_thread_pool       | 947 us                                                 | 792 us: 1.20x faster                                                        |
| sympy_str               | 328 ms                                                 | 275 ms: 1.19x faster                                                        |
| json_loads              | 28.8 us                                                | 24.1 us: 1.19x faster                                                       |
| dulwich_log             | 75.9 ms                                                | 63.9 ms: 1.19x faster                                                       |
| sympy_expand            | 545 ms                                                 | 460 ms: 1.18x faster                                                        |
| json                    | 5.42 ms                                                | 4.58 ms: 1.18x faster                                                       |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.17x faster                                                       |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                       |
| sympy_sum               | 185 ms                                                 | 160 ms: 1.15x faster                                                        |
| xml_etree_generate      | 94.2 ms                                                | 82.5 ms: 1.14x faster                                                       |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.49 sec: 1.13x faster                                                      |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                       |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                        |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.09x faster                                                        |
| pickle_list             | 4.56 us                                                | 4.26 us: 1.07x faster                                                       |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                                        |
| gc_traversal            | 3.84 ms                                                | 3.66 ms: 1.05x faster                                                       |
| unpickle                | 14.1 us                                                | 13.5 us: 1.05x faster                                                       |
| async_generators        | 425 ms                                                 | 411 ms: 1.03x faster                                                        |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| unpickle_list           | 4.82 us                                                | 5.13 us: 1.06x slower                                                       |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                       |
| regex_effbot            | 3.23 ms                                                | 3.67 ms: 1.14x slower                                                       |
| pickle_dict             | 27.3 us                                                | 31.8 us: 1.17x slower                                                       |
| dask                    | 423 ms                                                 | 503 ms: 1.19x slower                                                        |
| coverage                | 72.8 ms                                                | 95.3 ms: 1.31x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, telco
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
