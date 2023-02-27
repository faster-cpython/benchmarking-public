
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: d71edbd
- commit date: 2023-02-25
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.35x faster                                   |
| chameleon      | 9.17 ms                                                | 6.39 ms: 1.44x faster                                  |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                 |
| html5lib       | 85.9 ms                                                | 61.1 ms: 1.40x faster                                  |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 96.6 ms: 1.49x faster                                  |
| float          | 109 ms                                                 | 73.9 ms: 1.47x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.36x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                  |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.65 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                   |
| unpickle_pure_python | 302 us                                                 | 195 us: 1.55x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.45 ms: 1.42x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 55.0 ms: 1.36x faster                                  |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.3 ms: 1.17x faster                                  |
| pickle_list          | 4.72 us                                                | 4.19 us: 1.13x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 99.3 ms: 1.12x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                  |
| unpickle_list        | 4.92 us                                                | 5.02 us: 1.02x slower                                  |
| pickle               | 10.2 us                                                | 10.4 us: 1.03x slower                                  |
| pickle_dict          | 27.6 us                                                | 31.7 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.01 ms: 1.56x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.54 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.4 ms: 1.50x faster                                  |
| mako            | 14.7 ms                                                | 9.89 ms: 1.48x faster                                  |
| django_template | 46.3 ms                                                | 33.0 ms: 1.40x faster                                  |
| genshi_xml      | 63.7 ms                                                | 46.3 ms: 1.38x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230225-linux-x86_64-python-main-3.12.0a5+-d71edbd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.6 ms: 2.58x faster                                  |
| deltablue               | 7.28 ms                                                | 3.14 ms: 2.32x faster                                  |
| logging_silent          | 176 ns                                                 | 94.4 ns: 1.87x faster                                  |
| richards                | 75.2 ms                                                | 40.6 ms: 1.85x faster                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                   |
| asyncio_tcp             | 914 ms                                                 | 502 ms: 1.82x faster                                   |
| go                      | 226 ms                                                 | 133 ms: 1.69x faster                                   |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                   |
| pyflate                 | 676 ms                                                 | 407 ms: 1.66x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 66.0 ms: 1.64x faster                                  |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                   |
| chaos                   | 106 ms                                                 | 67.0 ms: 1.58x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.01 ms: 1.57x faster                                  |
| python_startup          | 14.1 ms                                                | 9.01 ms: 1.56x faster                                  |
| crypto_pyaes            | 117 ms                                                 | 74.7 ms: 1.56x faster                                  |
| spectral_norm           | 150 ms                                                 | 96.4 ms: 1.55x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 195 us: 1.55x faster                                   |
| genshi_text             | 30.6 ms                                                | 20.4 ms: 1.50x faster                                  |
| nbody                   | 144 ms                                                 | 96.6 ms: 1.49x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                  |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.48x faster                                   |
| mako                    | 14.7 ms                                                | 9.89 ms: 1.48x faster                                  |
| float                   | 109 ms                                                 | 73.9 ms: 1.47x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                  |
| chameleon               | 9.17 ms                                                | 6.39 ms: 1.44x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.45 ms: 1.42x faster                                  |
| logging_simple          | 8.10 us                                                | 5.72 us: 1.42x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                 |
| html5lib                | 85.9 ms                                                | 61.1 ms: 1.40x faster                                  |
| logging_format          | 8.85 us                                                | 6.31 us: 1.40x faster                                  |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                 |
| unpack_sequence         | 59.4 ns                                                | 42.4 ns: 1.40x faster                                  |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.40x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 681 ms: 1.40x faster                                   |
| genshi_xml              | 63.7 ms                                                | 46.3 ms: 1.38x faster                                  |
| coroutines              | 31.6 ms                                                | 23.0 ms: 1.38x faster                                  |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                 |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                  |
| regex_compile           | 177 ms                                                 | 131 ms: 1.36x faster                                   |
| xml_etree_process       | 74.5 ms                                                | 55.0 ms: 1.36x faster                                  |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                   |
| 2to3                    | 335 ms                                                 | 248 ms: 1.35x faster                                   |
| thrift                  | 1.03 ms                                                | 771 us: 1.34x faster                                   |
| fannkuch                | 488 ms                                                 | 364 ms: 1.34x faster                                   |
| async_tree_memoization  | 855 ms                                                 | 640 ms: 1.34x faster                                   |
| scimark_fft             | 421 ms                                                 | 317 ms: 1.33x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                  |
| deepcopy                | 438 us                                                 | 332 us: 1.32x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.31x faster                                   |
| mypy2                   | 430 ms                                                 | 332 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.5 ms: 1.29x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 739 ms: 1.28x faster                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.99 us: 1.27x faster                                  |
| nqueens                 | 100 ms                                                 | 80.0 ms: 1.25x faster                                  |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                 |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.7 ms: 1.21x faster                                  |
| dulwich_log             | 75.8 ms                                                | 63.1 ms: 1.20x faster                                  |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                  |
| bench_thread_pool       | 946 us                                                 | 787 us: 1.20x faster                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.62 ms: 1.18x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                  |
| json                    | 5.35 ms                                                | 4.54 ms: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.17x faster                                   |
| xml_etree_generate      | 93.8 ms                                                | 80.3 ms: 1.17x faster                                  |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                  |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                   |
| djangocms               | 36.9 us                                                | 32.5 us: 1.14x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| pickle_list             | 4.72 us                                                | 4.19 us: 1.13x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 99.3 ms: 1.12x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.11x faster                                  |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                   |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                  |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                  |
| mdp                     | 2.74 sec                                               | 2.66 sec: 1.03x faster                                 |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                   |
| telco                   | 6.73 ms                                                | 6.57 ms: 1.02x faster                                  |
| async_generators        | 426 ms                                                 | 420 ms: 1.02x faster                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| unpickle_list           | 4.92 us                                                | 5.02 us: 1.02x slower                                  |
| pickle                  | 10.2 us                                                | 10.4 us: 1.03x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.83 ms: 1.09x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.54 ms: 1.13x slower                                  |
| regex_effbot            | 3.19 ms                                                | 3.65 ms: 1.14x slower                                  |
| dask                    | 436 ms                                                 | 499 ms: 1.14x slower                                   |
| pickle_dict             | 27.6 us                                                | 31.7 us: 1.15x slower                                  |
| coverage                | 74.7 ms                                                | 96.5 ms: 1.29x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
