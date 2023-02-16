
# Results vs. 3.10.4

- fork: brandtbucher
- ref: quicken_at_runtime
- machine: linux-x86_64
- commit hash: 57469f4
- commit date: 2023-01-28
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 254 ms: 1.32x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.40 ms: 1.43x faster                                                      |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                     |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.3 ms: 1.56x faster                                                      |
| float          | 109 ms                                                 | 75.1 ms: 1.45x faster                                                      |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.36x faster                                                       |
| regex_v8       | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                      |
| regex_dna      | 214 ms                                                 | 219 ms: 1.03x slower                                                       |
| regex_effbot   | 3.19 ms                                                | 3.60 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 292 us: 1.55x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 208 us: 1.45x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 77.5 ms: 1.21x faster                                                      |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.06 us: 1.16x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                       |
| pickle               | 10.2 us                                                | 9.98 us: 1.02x faster                                                      |
| unpickle_list        | 4.92 us                                                | 5.07 us: 1.03x slower                                                      |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.70 ms: 1.62x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.23 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.44 ms: 1.55x faster                                                      |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.49x faster                                                      |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 46.4 ms: 1.37x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.35 ms: 2.17x faster                                                      |
| logging_silent          | 176 ns                                                 | 90.2 ns: 1.96x faster                                                      |
| asyncio_tcp             | 914 ms                                                 | 496 ms: 1.84x faster                                                       |
| richards                | 75.2 ms                                                | 42.9 ms: 1.75x faster                                                      |
| scimark_sor             | 197 ms                                                 | 118 ms: 1.66x faster                                                       |
| raytrace                | 467 ms                                                 | 282 ms: 1.65x faster                                                       |
| python_startup          | 14.1 ms                                                | 8.70 ms: 1.62x faster                                                      |
| scimark_monte_carlo     | 109 ms                                                 | 67.3 ms: 1.61x faster                                                      |
| go                      | 226 ms                                                 | 140 ms: 1.61x faster                                                       |
| crypto_pyaes            | 117 ms                                                 | 72.6 ms: 1.61x faster                                                      |
| chaos                   | 106 ms                                                 | 65.9 ms: 1.60x faster                                                      |
| pyflate                 | 676 ms                                                 | 432 ms: 1.56x faster                                                       |
| nbody                   | 144 ms                                                 | 92.3 ms: 1.56x faster                                                      |
| spectral_norm           | 150 ms                                                 | 96.1 ms: 1.56x faster                                                      |
| mako                    | 14.7 ms                                                | 9.44 ms: 1.55x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 292 us: 1.55x faster                                                       |
| hexiom                  | 9.43 ms                                                | 6.16 ms: 1.53x faster                                                      |
| scimark_lu              | 161 ms                                                 | 105 ms: 1.53x faster                                                       |
| deepcopy_memo           | 51.7 us                                                | 34.0 us: 1.52x faster                                                      |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.49x faster                                                      |
| float                   | 109 ms                                                 | 75.1 ms: 1.45x faster                                                      |
| unpickle_pure_python    | 302 us                                                 | 208 us: 1.45x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.40 ms: 1.43x faster                                                      |
| json_dumps              | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                      |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 41.7 ns: 1.42x faster                                                      |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                                     |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                                      |
| logging_simple          | 8.10 us                                                | 5.75 us: 1.41x faster                                                      |
| pprint_safe_repr        | 953 ms                                                 | 681 ms: 1.40x faster                                                       |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                                      |
| scimark_fft             | 421 ms                                                 | 302 ms: 1.40x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 53.6 ms: 1.39x faster                                                      |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                                       |
| logging_format          | 8.85 us                                                | 6.37 us: 1.39x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.94 ms: 1.38x faster                                                      |
| genshi_xml              | 63.7 ms                                                | 46.4 ms: 1.37x faster                                                      |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                     |
| async_tree_none         | 711 ms                                                 | 522 ms: 1.36x faster                                                       |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                                      |
| regex_compile           | 177 ms                                                 | 131 ms: 1.36x faster                                                       |
| deepcopy                | 438 us                                                 | 324 us: 1.35x faster                                                       |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                      |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                                      |
| pycparser               | 1.53 sec                                               | 1.16 sec: 1.32x faster                                                     |
| 2to3                    | 335 ms                                                 | 254 ms: 1.32x faster                                                       |
| deepcopy_reduce         | 3.79 us                                                | 2.91 us: 1.30x faster                                                      |
| async_tree_memoization  | 855 ms                                                 | 661 ms: 1.29x faster                                                       |
| nqueens                 | 100 ms                                                 | 78.0 ms: 1.28x faster                                                      |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                                      |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                       |
| fannkuch                | 488 ms                                                 | 385 ms: 1.27x faster                                                       |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                     |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                       |
| coroutines              | 31.6 ms                                                | 26.0 ms: 1.22x faster                                                      |
| xml_etree_generate      | 93.8 ms                                                | 77.5 ms: 1.21x faster                                                      |
| bench_thread_pool       | 946 us                                                 | 783 us: 1.21x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 20.0 ms: 1.20x faster                                                      |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.20x faster                                                      |
| sympy_str               | 325 ms                                                 | 270 ms: 1.20x faster                                                       |
| async_generators        | 426 ms                                                 | 355 ms: 1.20x faster                                                       |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                      |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                       |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.17x faster                                                       |
| pickle_list             | 4.72 us                                                | 4.06 us: 1.16x faster                                                      |
| json                    | 5.35 ms                                                | 4.61 ms: 1.16x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.45 ms: 1.14x faster                                                      |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                                      |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.45 sec: 1.12x faster                                                     |
| regex_v8                | 25.0 ms                                                | 22.7 ms: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                       |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                                      |
| telco                   | 6.73 ms                                                | 6.34 ms: 1.06x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                       |
| generators              | 76.4 ms                                                | 74.4 ms: 1.03x faster                                                      |
| pickle                  | 10.2 us                                                | 9.98 us: 1.02x faster                                                      |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                       |
| regex_dna               | 214 ms                                                 | 219 ms: 1.03x slower                                                       |
| unpickle_list           | 4.92 us                                                | 5.07 us: 1.03x slower                                                      |
| gc_traversal            | 3.53 ms                                                | 3.76 ms: 1.07x slower                                                      |
| python_startup_no_site  | 5.78 ms                                                | 6.23 ms: 1.08x slower                                                      |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.60 ms: 1.13x slower                                                      |
| dask                    | 436 ms                                                 | 511 ms: 1.17x slower                                                       |
| coverage                | 74.7 ms                                                | 102 ms: 1.36x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230128-3.12.0a4+-57469f4/bm-20230128-linux-x86_64-brandtbucher-quicken_at_runtime-3.12.0a4+-57469f4.json: mypy
