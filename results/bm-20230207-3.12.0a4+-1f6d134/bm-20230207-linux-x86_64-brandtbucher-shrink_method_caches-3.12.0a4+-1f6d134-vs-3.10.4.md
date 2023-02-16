
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_method_caches
- machine: linux-x86_64
- commit hash: 1f6d134
- commit date: 2023-02-07
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.33x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.58 ms: 1.39x faster                                                        |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| tornado_http   | 128 ms                                                 | 96.2 ms: 1.33x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.8 ms: 1.50x faster                                                        |
| float          | 109 ms                                                 | 74.0 ms: 1.47x faster                                                        |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.38x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                        |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                         |
| regex_effbot   | 3.19 ms                                                | 3.76 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 292 us: 1.55x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.52x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.47 ms: 1.42x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 53.8 ms: 1.38x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 77.6 ms: 1.21x faster                                                        |
| json_loads           | 28.7 us                                                | 23.8 us: 1.21x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.05 us: 1.16x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                         |
| pickle               | 10.2 us                                                | 9.96 us: 1.02x faster                                                        |
| unpickle_list        | 4.92 us                                                | 5.04 us: 1.02x slower                                                        |
| pickle_dict          | 27.6 us                                                | 30.0 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.94 ms: 1.58x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.45 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.98 ms: 1.47x faster                                                        |
| genshi_text     | 30.6 ms                                                | 21.0 ms: 1.46x faster                                                        |
| django_template | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 47.3 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-brandtbucher-shrink_method_caches-3.12.0a4+-1f6d134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.35 ms: 2.17x faster                                                        |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.85x faster                                                         |
| asyncio_tcp             | 914 ms                                                 | 496 ms: 1.84x faster                                                         |
| logging_silent          | 176 ns                                                 | 99.9 ns: 1.77x faster                                                        |
| richards                | 75.2 ms                                                | 44.6 ms: 1.69x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 65.8 ms: 1.65x faster                                                        |
| pyflate                 | 676 ms                                                 | 412 ms: 1.64x faster                                                         |
| raytrace                | 467 ms                                                 | 288 ms: 1.62x faster                                                         |
| go                      | 226 ms                                                 | 140 ms: 1.61x faster                                                         |
| chaos                   | 106 ms                                                 | 65.9 ms: 1.60x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 73.7 ms: 1.58x faster                                                        |
| spectral_norm           | 150 ms                                                 | 94.6 ms: 1.58x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.94 ms: 1.58x faster                                                        |
| hexiom                  | 9.43 ms                                                | 6.02 ms: 1.57x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 292 us: 1.55x faster                                                         |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.52x faster                                                         |
| nbody                   | 144 ms                                                 | 95.8 ms: 1.50x faster                                                        |
| float                   | 109 ms                                                 | 74.0 ms: 1.47x faster                                                        |
| mako                    | 14.7 ms                                                | 9.98 ms: 1.47x faster                                                        |
| genshi_text             | 30.6 ms                                                | 21.0 ms: 1.46x faster                                                        |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.45x faster                                                         |
| deepcopy_memo           | 51.7 us                                                | 35.7 us: 1.45x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.47 ms: 1.42x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                                        |
| logging_simple          | 8.10 us                                                | 5.78 us: 1.40x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                                       |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.39x faster                                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.39x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 684 ms: 1.39x faster                                                         |
| chameleon               | 9.17 ms                                                | 6.58 ms: 1.39x faster                                                        |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 53.8 ms: 1.38x faster                                                        |
| regex_compile           | 177 ms                                                 | 128 ms: 1.38x faster                                                         |
| logging_format          | 8.85 us                                                | 6.46 us: 1.37x faster                                                        |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.35x faster                                                         |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                       |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                         |
| genshi_xml              | 63.7 ms                                                | 47.3 ms: 1.35x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 44.2 ns: 1.34x faster                                                        |
| fannkuch                | 488 ms                                                 | 365 ms: 1.33x faster                                                         |
| tornado_http            | 128 ms                                                 | 96.2 ms: 1.33x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.11 ms: 1.33x faster                                                        |
| 2to3                    | 335 ms                                                 | 253 ms: 1.33x faster                                                         |
| aiohttp                 | 1.34 ms                                                | 1.02 ms: 1.32x faster                                                        |
| nqueens                 | 100 ms                                                 | 76.5 ms: 1.31x faster                                                        |
| gunicorn                | 1.43 ms                                                | 1.10 ms: 1.30x faster                                                        |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                         |
| async_tree_memoization  | 855 ms                                                 | 664 ms: 1.29x faster                                                         |
| deepcopy                | 438 us                                                 | 343 us: 1.27x faster                                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 753 ms: 1.26x faster                                                         |
| deepcopy_reduce         | 3.79 us                                                | 3.01 us: 1.26x faster                                                        |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 52.0 ms: 1.25x faster                                                        |
| coroutines              | 31.6 ms                                                | 25.3 ms: 1.25x faster                                                        |
| sqlglot_normalize       | 134 ms                                                 | 108 ms: 1.25x faster                                                         |
| xml_etree_generate      | 93.8 ms                                                | 77.6 ms: 1.21x faster                                                        |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.8 ms: 1.21x faster                                                        |
| json_loads              | 28.7 us                                                | 23.8 us: 1.21x faster                                                        |
| async_generators        | 426 ms                                                 | 354 ms: 1.20x faster                                                         |
| sympy_integrate         | 24.0 ms                                                | 20.0 ms: 1.20x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                         |
| bench_thread_pool       | 946 us                                                 | 795 us: 1.19x faster                                                         |
| sympy_str               | 325 ms                                                 | 274 ms: 1.19x faster                                                         |
| dulwich_log             | 75.8 ms                                                | 64.5 ms: 1.18x faster                                                        |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                         |
| pickle_list             | 4.72 us                                                | 4.05 us: 1.16x faster                                                        |
| sympy_sum               | 183 ms                                                 | 157 ms: 1.16x faster                                                         |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                        |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                        |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                        |
| json                    | 5.35 ms                                                | 4.79 ms: 1.12x faster                                                        |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                         |
| mdp                     | 2.74 sec                                               | 2.48 sec: 1.11x faster                                                       |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                         |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                         |
| telco                   | 6.73 ms                                                | 6.40 ms: 1.05x faster                                                        |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                         |
| pickle                  | 10.2 us                                                | 9.96 us: 1.02x faster                                                        |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                         |
| unpickle_list           | 4.92 us                                                | 5.04 us: 1.02x slower                                                        |
| generators              | 76.4 ms                                                | 78.6 ms: 1.03x slower                                                        |
| pickle_dict             | 27.6 us                                                | 30.0 us: 1.09x slower                                                        |
| gc_traversal            | 3.53 ms                                                | 3.88 ms: 1.10x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.45 ms: 1.12x slower                                                        |
| dask                    | 436 ms                                                 | 502 ms: 1.15x slower                                                         |
| regex_effbot            | 3.19 ms                                                | 3.76 ms: 1.18x slower                                                        |
| coverage                | 74.7 ms                                                | 99.2 ms: 1.33x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.28x faster                                                                 |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
