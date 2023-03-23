
# Results vs. 3.10.4

- fork: brandtbucher
- ref: type_cache_fixed
- machine: linux-x86_64
- commit hash: 212046c
- commit date: 2023-03-23
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                     |
| chameleon      | 9.17 ms                                                | 6.48 ms: 1.41x faster                                                    |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                   |
| html5lib       | 85.9 ms                                                | 61.6 ms: 1.39x faster                                                    |
| tornado_http   | 128 ms                                                 | 92.5 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 87.8 ms: 1.64x faster                                                    |
| float          | 109 ms                                                 | 73.1 ms: 1.49x faster                                                    |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                     |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                    |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                                     |
| regex_effbot   | 3.19 ms                                                | 3.37 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                                     |
| unpickle_pure_python | 302 us                                                 | 200 us: 1.51x faster                                                     |
| json_dumps           | 13.4 ms                                                | 9.56 ms: 1.41x faster                                                    |
| xml_etree_process    | 74.5 ms                                                | 56.0 ms: 1.33x faster                                                    |
| json_loads           | 28.7 us                                                | 24.2 us: 1.19x faster                                                    |
| xml_etree_generate   | 93.8 ms                                                | 80.9 ms: 1.16x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 99.2 ms: 1.12x faster                                                    |
| pickle_list          | 4.72 us                                                | 4.27 us: 1.11x faster                                                    |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                     |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                                    |
| pickle               | 10.2 us                                                | 10.4 us: 1.03x slower                                                    |
| unpickle_list        | 4.92 us                                                | 5.25 us: 1.07x slower                                                    |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.82 ms: 1.60x faster                                                    |
| python_startup_no_site | 5.78 ms                                                | 6.53 ms: 1.13x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.1 ms: 1.45x faster                                                    |
| genshi_text     | 30.6 ms                                                | 21.6 ms: 1.42x faster                                                    |
| django_template | 46.3 ms                                                | 33.0 ms: 1.41x faster                                                    |
| genshi_xml      | 63.7 ms                                                | 48.4 ms: 1.32x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.8 ms: 2.57x faster                                                    |
| deltablue               | 7.28 ms                                                | 3.27 ms: 2.22x faster                                                    |
| logging_silent          | 176 ns                                                 | 97.5 ns: 1.81x faster                                                    |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.80x faster                                                     |
| asyncio_tcp             | 914 ms                                                 | 510 ms: 1.79x faster                                                     |
| richards                | 75.2 ms                                                | 44.1 ms: 1.70x faster                                                    |
| go                      | 226 ms                                                 | 133 ms: 1.69x faster                                                     |
| spectral_norm           | 150 ms                                                 | 90.9 ms: 1.65x faster                                                    |
| nbody                   | 144 ms                                                 | 87.8 ms: 1.64x faster                                                    |
| scimark_monte_carlo     | 109 ms                                                 | 67.0 ms: 1.62x faster                                                    |
| raytrace                | 467 ms                                                 | 288 ms: 1.62x faster                                                     |
| pyflate                 | 676 ms                                                 | 418 ms: 1.62x faster                                                     |
| python_startup          | 14.1 ms                                                | 8.82 ms: 1.60x faster                                                    |
| chaos                   | 106 ms                                                 | 66.6 ms: 1.59x faster                                                    |
| crypto_pyaes            | 117 ms                                                 | 73.8 ms: 1.58x faster                                                    |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                                     |
| hexiom                  | 9.43 ms                                                | 6.08 ms: 1.55x faster                                                    |
| unpickle_pure_python    | 302 us                                                 | 200 us: 1.51x faster                                                     |
| float                   | 109 ms                                                 | 73.1 ms: 1.49x faster                                                    |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                                    |
| mako                    | 14.7 ms                                                | 10.1 ms: 1.45x faster                                                    |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.44x faster                                                     |
| unpack_sequence         | 59.4 ns                                                | 41.7 ns: 1.42x faster                                                    |
| genshi_text             | 30.6 ms                                                | 21.6 ms: 1.42x faster                                                    |
| chameleon               | 9.17 ms                                                | 6.48 ms: 1.41x faster                                                    |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                                    |
| json_dumps              | 13.4 ms                                                | 9.56 ms: 1.41x faster                                                    |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.41x faster                                                    |
| coroutines              | 31.6 ms                                                | 22.6 ms: 1.40x faster                                                    |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.39x faster                                                    |
| html5lib                | 85.9 ms                                                | 61.6 ms: 1.39x faster                                                    |
| pprint_safe_repr        | 953 ms                                                 | 686 ms: 1.39x faster                                                     |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                   |
| tornado_http            | 128 ms                                                 | 92.5 ms: 1.39x faster                                                    |
| logging_format          | 8.85 us                                                | 6.46 us: 1.37x faster                                                    |
| logging_simple          | 8.10 us                                                | 5.91 us: 1.37x faster                                                    |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                                   |
| async_tree_none         | 711 ms                                                 | 525 ms: 1.36x faster                                                     |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                     |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                     |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                     |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                    |
| xml_etree_process       | 74.5 ms                                                | 56.0 ms: 1.33x faster                                                    |
| deepcopy                | 438 us                                                 | 330 us: 1.32x faster                                                     |
| fannkuch                | 488 ms                                                 | 370 ms: 1.32x faster                                                     |
| genshi_xml              | 63.7 ms                                                | 48.4 ms: 1.32x faster                                                    |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                    |
| thrift                  | 1.03 ms                                                | 792 us: 1.31x faster                                                     |
| mypy2                   | 430 ms                                                 | 335 ms: 1.28x faster                                                     |
| async_tree_memoization  | 855 ms                                                 | 673 ms: 1.27x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.29 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed | 949 ms                                                 | 749 ms: 1.27x faster                                                     |
| deepcopy_reduce         | 3.79 us                                                | 3.00 us: 1.26x faster                                                    |
| nqueens                 | 100 ms                                                 | 79.4 ms: 1.26x faster                                                    |
| sqlglot_optimize        | 65.2 ms                                                | 51.8 ms: 1.26x faster                                                    |
| sqlglot_normalize       | 134 ms                                                 | 107 ms: 1.26x faster                                                     |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.26x faster                                                   |
| bench_thread_pool       | 946 us                                                 | 794 us: 1.19x faster                                                     |
| dulwich_log             | 75.8 ms                                                | 63.8 ms: 1.19x faster                                                    |
| json_loads              | 28.7 us                                                | 24.2 us: 1.19x faster                                                    |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                                    |
| sympy_expand            | 534 ms                                                 | 460 ms: 1.16x faster                                                     |
| xml_etree_generate      | 93.8 ms                                                | 80.9 ms: 1.16x faster                                                    |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                    |
| sympy_str               | 325 ms                                                 | 284 ms: 1.14x faster                                                     |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                                    |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                    |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                    |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 99.2 ms: 1.12x faster                                                    |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.11x faster                                                    |
| pickle_list             | 4.72 us                                                | 4.27 us: 1.11x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                     |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                                     |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                     |
| mdp                     | 2.74 sec                                               | 2.51 sec: 1.09x faster                                                   |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                                     |
| telco                   | 6.73 ms                                                | 6.45 ms: 1.04x faster                                                    |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                                    |
| async_generators        | 426 ms                                                 | 416 ms: 1.02x faster                                                     |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                     |
| gc_traversal            | 3.53 ms                                                | 3.53 ms: 1.00x slower                                                    |
| pickle                  | 10.2 us                                                | 10.4 us: 1.03x slower                                                    |
| regex_effbot            | 3.19 ms                                                | 3.37 ms: 1.06x slower                                                    |
| unpickle_list           | 4.92 us                                                | 5.25 us: 1.07x slower                                                    |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                                    |
| python_startup_no_site  | 5.78 ms                                                | 6.53 ms: 1.13x slower                                                    |
| dask                    | 436 ms                                                 | 512 ms: 1.17x slower                                                     |
| coverage                | 74.7 ms                                                | 97.0 ms: 1.30x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230323-3.12.0a6+-212046c/bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed-3.12.0a6+-212046c.json: comprehensions
