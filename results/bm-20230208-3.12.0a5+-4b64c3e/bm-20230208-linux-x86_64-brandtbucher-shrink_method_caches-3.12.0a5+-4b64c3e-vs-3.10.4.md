
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 4b64c3e
- commit date: 2023-02-08
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.36 ms: 1.44x faster                                                        |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.8 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.1 ms: 1.55x faster                                                        |
| float          | 109 ms                                                 | 73.0 ms: 1.49x faster                                                        |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                        |
| regex_dna      | 214 ms                                                 | 218 ms: 1.02x slower                                                         |
| regex_effbot   | 3.19 ms                                                | 3.52 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 294 us: 1.54x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.51x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.33 ms: 1.44x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 55.3 ms: 1.35x faster                                                        |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 80.5 ms: 1.16x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.13 us: 1.14x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                         |
| unpickle             | 14.2 us                                                | 13.7 us: 1.04x faster                                                        |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                                        |
| pickle_dict          | 27.6 us                                                | 30.4 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.86 ms: 1.59x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.42 ms: 1.11x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.90 ms: 1.48x faster                                                        |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                        |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a5+-4b64c3e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.19 ms: 2.28x faster                                                        |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.84x faster                                                         |
| logging_silent          | 176 ns                                                 | 95.9 ns: 1.84x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 505 ms: 1.81x faster                                                         |
| richards                | 75.2 ms                                                | 42.8 ms: 1.76x faster                                                        |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                         |
| pyflate                 | 676 ms                                                 | 406 ms: 1.67x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                 | 66.1 ms: 1.64x faster                                                        |
| raytrace                | 467 ms                                                 | 286 ms: 1.63x faster                                                         |
| spectral_norm           | 150 ms                                                 | 93.4 ms: 1.60x faster                                                        |
| chaos                   | 106 ms                                                 | 66.4 ms: 1.59x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.86 ms: 1.59x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 73.6 ms: 1.58x faster                                                        |
| hexiom                  | 9.43 ms                                                | 5.96 ms: 1.58x faster                                                        |
| nbody                   | 144 ms                                                 | 93.1 ms: 1.55x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 294 us: 1.54x faster                                                         |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.51x faster                                                         |
| deepcopy_memo           | 51.7 us                                                | 34.5 us: 1.50x faster                                                        |
| float                   | 109 ms                                                 | 73.0 ms: 1.49x faster                                                        |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                         |
| mako                    | 14.7 ms                                                | 9.90 ms: 1.48x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.36 ms: 1.44x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.33 ms: 1.44x faster                                                        |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.42 sec: 1.40x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.40x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 686 ms: 1.39x faster                                                         |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                         |
| scimark_fft             | 421 ms                                                 | 308 ms: 1.37x faster                                                         |
| logging_format          | 8.85 us                                                | 6.49 us: 1.36x faster                                                        |
| thrift                  | 1.03 ms                                                | 759 us: 1.36x faster                                                         |
| logging_simple          | 8.10 us                                                | 5.95 us: 1.36x faster                                                        |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                         |
| genshi_xml              | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                                       |
| tornado_http            | 128 ms                                                 | 94.8 ms: 1.35x faster                                                        |
| fannkuch                | 488 ms                                                 | 361 ms: 1.35x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 55.3 ms: 1.35x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 44.2 ns: 1.34x faster                                                        |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                         |
| async_tree_memoization  | 855 ms                                                 | 645 ms: 1.33x faster                                                         |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                                         |
| aiohttp                 | 1.34 ms                                                | 1.02 ms: 1.32x faster                                                        |
| nqueens                 | 100 ms                                                 | 76.2 ms: 1.31x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.30x faster                                                        |
| mypy2                   | 430 ms                                                 | 331 ms: 1.30x faster                                                         |
| coroutines              | 31.6 ms                                                | 24.5 ms: 1.29x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.27 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 749 ms: 1.27x faster                                                         |
| sqlglot_optimize        | 65.2 ms                                                | 51.8 ms: 1.26x faster                                                        |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                       |
| sqlglot_normalize       | 134 ms                                                 | 108 ms: 1.25x faster                                                         |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                                         |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                        |
| sympy_str               | 325 ms                                                 | 271 ms: 1.20x faster                                                         |
| bench_thread_pool       | 946 us                                                 | 791 us: 1.20x faster                                                         |
| dulwich_log             | 75.8 ms                                                | 63.6 ms: 1.19x faster                                                        |
| sympy_expand            | 534 ms                                                 | 452 ms: 1.18x faster                                                         |
| xml_etree_generate      | 93.8 ms                                                | 80.5 ms: 1.16x faster                                                        |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.4 ms: 1.16x faster                                                        |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                                         |
| json                    | 5.35 ms                                                | 4.66 ms: 1.15x faster                                                        |
| pickle_list             | 4.72 us                                                | 4.13 us: 1.14x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                        |
| djangocms               | 36.9 us                                                | 32.5 us: 1.14x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                        |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                        |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                        |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                         |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                         |
| telco                   | 6.73 ms                                                | 6.41 ms: 1.05x faster                                                        |
| unpickle                | 14.2 us                                                | 13.7 us: 1.04x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.70 sec: 1.02x faster                                                       |
| generators              | 76.4 ms                                                | 76.9 ms: 1.01x slower                                                        |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                                        |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| regex_dna               | 214 ms                                                 | 218 ms: 1.02x slower                                                         |
| async_generators        | 426 ms                                                 | 435 ms: 1.02x slower                                                         |
| gc_traversal            | 3.53 ms                                                | 3.65 ms: 1.03x slower                                                        |
| pickle_dict             | 27.6 us                                                | 30.4 us: 1.10x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.52 ms: 1.10x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.42 ms: 1.11x slower                                                        |
| coverage                | 74.7 ms                                                | 101 ms: 1.35x slower                                                         |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                 |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
