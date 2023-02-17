
# Results vs. 3.10.4

- fork: brandtbucher
- ref: replicate_load_fast
- machine: linux-x86_64
- commit hash: 7dd73c5
- commit date: 2023-02-16
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.36x faster                                                        |
| chameleon      | 9.17 ms                                                | 6.34 ms: 1.45x faster                                                       |
| docutils       | 3.18 sec                                               | 2.57 sec: 1.23x faster                                                      |
| html5lib       | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                       |
| tornado_http   | 128 ms                                                 | 95.5 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.2 ms: 1.54x faster                                                       |
| float          | 109 ms                                                 | 72.6 ms: 1.50x faster                                                       |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.35x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                       |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                        |
| regex_effbot   | 3.19 ms                                                | 3.67 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                                        |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.51x faster                                                        |
| json_dumps           | 13.4 ms                                                | 9.66 ms: 1.39x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 56.5 ms: 1.32x faster                                                       |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                       |
| xml_etree_generate   | 93.8 ms                                                | 82.5 ms: 1.14x faster                                                       |
| pickle_list          | 4.72 us                                                | 4.26 us: 1.11x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| unpickle             | 14.2 us                                                | 13.5 us: 1.05x faster                                                       |
| unpickle_list        | 4.92 us                                                | 5.13 us: 1.04x slower                                                       |
| pickle_dict          | 27.6 us                                                | 31.8 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.00 ms: 1.56x faster                                                       |
| python_startup_no_site | 5.78 ms                                                | 6.53 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.67 ms: 1.52x faster                                                       |
| genshi_text     | 30.6 ms                                                | 21.1 ms: 1.45x faster                                                       |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                       |
| genshi_xml      | 63.7 ms                                                | 47.4 ms: 1.35x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230216-linux-x86_64-brandtbucher-replicate_load_fast-3.12.0a5+-7dd73c5 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.6 ms: 2.50x faster                                                       |
| deltablue               | 7.28 ms                                                | 3.22 ms: 2.26x faster                                                       |
| logging_silent          | 176 ns                                                 | 94.1 ns: 1.88x faster                                                       |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 505 ms: 1.81x faster                                                        |
| richards                | 75.2 ms                                                | 42.3 ms: 1.78x faster                                                       |
| pyflate                 | 676 ms                                                 | 406 ms: 1.67x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 65.2 ms: 1.66x faster                                                       |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                                        |
| raytrace                | 467 ms                                                 | 288 ms: 1.62x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                                        |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.60x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 73.5 ms: 1.59x faster                                                       |
| chaos                   | 106 ms                                                 | 67.3 ms: 1.57x faster                                                       |
| python_startup          | 14.1 ms                                                | 9.00 ms: 1.56x faster                                                       |
| nbody                   | 144 ms                                                 | 93.2 ms: 1.54x faster                                                       |
| mako                    | 14.7 ms                                                | 9.67 ms: 1.52x faster                                                       |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.51x faster                                                        |
| hexiom                  | 9.43 ms                                                | 6.24 ms: 1.51x faster                                                       |
| float                   | 109 ms                                                 | 72.6 ms: 1.50x faster                                                       |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 35.0 us: 1.47x faster                                                       |
| genshi_text             | 30.6 ms                                                | 21.1 ms: 1.45x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.34 ms: 1.45x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 41.4 ns: 1.43x faster                                                       |
| logging_simple          | 8.10 us                                                | 5.69 us: 1.42x faster                                                       |
| coroutines              | 31.6 ms                                                | 22.2 ms: 1.42x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                                       |
| logging_format          | 8.85 us                                                | 6.28 us: 1.41x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.40x faster                                                      |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.40x faster                                                       |
| json_dumps              | 13.4 ms                                                | 9.66 ms: 1.39x faster                                                       |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                      |
| html5lib                | 85.9 ms                                                | 61.8 ms: 1.39x faster                                                       |
| pprint_safe_repr        | 953 ms                                                 | 692 ms: 1.38x faster                                                        |
| thrift                  | 1.03 ms                                                | 760 us: 1.36x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                      |
| 2to3                    | 335 ms                                                 | 248 ms: 1.36x faster                                                        |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                                       |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                        |
| regex_compile           | 177 ms                                                 | 132 ms: 1.35x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 47.4 ms: 1.35x faster                                                       |
| tornado_http            | 128 ms                                                 | 95.5 ms: 1.34x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                       |
| fannkuch                | 488 ms                                                 | 368 ms: 1.32x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 646 ms: 1.32x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 56.5 ms: 1.32x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                       |
| deepcopy                | 438 us                                                 | 335 us: 1.31x faster                                                        |
| mypy2                   | 430 ms                                                 | 335 ms: 1.28x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 740 ms: 1.28x faster                                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 51.2 ms: 1.27x faster                                                       |
| nqueens                 | 100 ms                                                 | 79.5 ms: 1.26x faster                                                       |
| docutils                | 3.18 sec                                               | 2.57 sec: 1.23x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 20.0 ms: 1.20x faster                                                       |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 792 us: 1.20x faster                                                        |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                                       |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                       |
| dulwich_log             | 75.8 ms                                                | 63.9 ms: 1.19x faster                                                       |
| sympy_str               | 325 ms                                                 | 275 ms: 1.18x faster                                                        |
| json                    | 5.35 ms                                                | 4.58 ms: 1.17x faster                                                       |
| sympy_expand            | 534 ms                                                 | 460 ms: 1.16x faster                                                        |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                       |
| sympy_sum               | 183 ms                                                 | 160 ms: 1.15x faster                                                        |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                       |
| xml_etree_generate      | 93.8 ms                                                | 82.5 ms: 1.14x faster                                                       |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                       |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                       |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.11x faster                                                       |
| pickle_list             | 4.72 us                                                | 4.26 us: 1.11x faster                                                       |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.49 sec: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| unpickle                | 14.2 us                                                | 13.5 us: 1.05x faster                                                       |
| async_generators        | 426 ms                                                 | 411 ms: 1.04x faster                                                        |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                        |
| telco                   | 6.73 ms                                                | 6.55 ms: 1.03x faster                                                       |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                        |
| gc_traversal            | 3.53 ms                                                | 3.66 ms: 1.04x slower                                                       |
| unpickle_list           | 4.92 us                                                | 5.13 us: 1.04x slower                                                       |
| python_startup_no_site  | 5.78 ms                                                | 6.53 ms: 1.13x slower                                                       |
| regex_effbot            | 3.19 ms                                                | 3.67 ms: 1.15x slower                                                       |
| dask                    | 436 ms                                                 | 503 ms: 1.15x slower                                                        |
| pickle_dict             | 27.6 us                                                | 31.8 us: 1.15x slower                                                       |
| coverage                | 74.7 ms                                                | 95.3 ms: 1.28x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
