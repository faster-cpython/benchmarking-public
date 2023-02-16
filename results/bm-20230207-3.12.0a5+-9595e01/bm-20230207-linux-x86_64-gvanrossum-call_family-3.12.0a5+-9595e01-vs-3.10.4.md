
# Results vs. 3.10.4

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: 9595e01
- commit date: 2023-02-07
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                              |
| chameleon      | 9.17 ms                                                | 6.36 ms: 1.44x faster                                             |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                            |
| html5lib       | 85.9 ms                                                | 61.1 ms: 1.41x faster                                             |
| tornado_http   | 128 ms                                                 | 93.7 ms: 1.37x faster                                             |
| Geometric mean | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 96.0 ms: 1.50x faster                                             |
| float          | 109 ms                                                 | 73.7 ms: 1.48x faster                                             |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.29x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                              |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                             |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                              |
| regex_effbot   | 3.19 ms                                                | 3.62 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 286 us: 1.58x faster                                              |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.52x faster                                              |
| json_dumps           | 13.4 ms                                                | 9.53 ms: 1.41x faster                                             |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                             |
| xml_etree_generate   | 93.8 ms                                                | 77.4 ms: 1.21x faster                                             |
| json_loads           | 28.7 us                                                | 24.3 us: 1.18x faster                                             |
| pickle_list          | 4.72 us                                                | 4.14 us: 1.14x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                              |
| unpickle             | 14.2 us                                                | 13.3 us: 1.07x faster                                             |
| unpickle_list        | 4.92 us                                                | 5.01 us: 1.02x slower                                             |
| pickle               | 10.2 us                                                | 10.4 us: 1.02x slower                                             |
| pickle_dict          | 27.6 us                                                | 31.6 us: 1.14x slower                                             |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.91 ms: 1.58x faster                                             |
| python_startup_no_site | 5.78 ms                                                | 6.47 ms: 1.12x slower                                             |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                             |
| mako            | 14.7 ms                                                | 9.92 ms: 1.48x faster                                             |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                             |
| genshi_xml      | 63.7 ms                                                | 46.5 ms: 1.37x faster                                             |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-linux-x86_64-gvanrossum-call_family-3.12.0a5+-9595e01 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.16 ms: 2.30x faster                                             |
| logging_silent          | 176 ns                                                 | 93.3 ns: 1.89x faster                                             |
| asyncio_tcp             | 914 ms                                                 | 492 ms: 1.86x faster                                              |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                              |
| richards                | 75.2 ms                                                | 42.2 ms: 1.78x faster                                             |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                              |
| pyflate                 | 676 ms                                                 | 404 ms: 1.67x faster                                              |
| raytrace                | 467 ms                                                 | 283 ms: 1.65x faster                                              |
| scimark_monte_carlo     | 109 ms                                                 | 66.2 ms: 1.64x faster                                             |
| crypto_pyaes            | 117 ms                                                 | 72.6 ms: 1.61x faster                                             |
| chaos                   | 106 ms                                                 | 66.1 ms: 1.60x faster                                             |
| pickle_pure_python      | 452 us                                                 | 286 us: 1.58x faster                                              |
| hexiom                  | 9.43 ms                                                | 5.96 ms: 1.58x faster                                             |
| python_startup          | 14.1 ms                                                | 8.91 ms: 1.58x faster                                             |
| spectral_norm           | 150 ms                                                 | 95.4 ms: 1.57x faster                                             |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.52x faster                                              |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                              |
| nbody                   | 144 ms                                                 | 96.0 ms: 1.50x faster                                             |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                             |
| float                   | 109 ms                                                 | 73.7 ms: 1.48x faster                                             |
| mako                    | 14.7 ms                                                | 9.92 ms: 1.48x faster                                             |
| deepcopy_memo           | 51.7 us                                                | 35.0 us: 1.48x faster                                             |
| chameleon               | 9.17 ms                                                | 6.36 ms: 1.44x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                             |
| unpack_sequence         | 59.4 ns                                                | 41.6 ns: 1.43x faster                                             |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                             |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                             |
| json_dumps              | 13.4 ms                                                | 9.53 ms: 1.41x faster                                             |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                            |
| thrift                  | 1.03 ms                                                | 735 us: 1.41x faster                                              |
| html5lib                | 85.9 ms                                                | 61.1 ms: 1.41x faster                                             |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                             |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                              |
| pprint_safe_repr        | 953 ms                                                 | 689 ms: 1.38x faster                                              |
| logging_simple          | 8.10 us                                                | 5.89 us: 1.38x faster                                             |
| fannkuch                | 488 ms                                                 | 355 ms: 1.37x faster                                              |
| genshi_xml              | 63.7 ms                                                | 46.5 ms: 1.37x faster                                             |
| tornado_http            | 128 ms                                                 | 93.7 ms: 1.37x faster                                             |
| logging_format          | 8.85 us                                                | 6.48 us: 1.37x faster                                             |
| async_tree_none         | 711 ms                                                 | 522 ms: 1.36x faster                                              |
| scimark_fft             | 421 ms                                                 | 309 ms: 1.36x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.35x faster                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.04 ms: 1.35x faster                                             |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                             |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                              |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                            |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                             |
| async_tree_memoization  | 855 ms                                                 | 647 ms: 1.32x faster                                              |
| mypy2                   | 430 ms                                                 | 330 ms: 1.30x faster                                              |
| deepcopy                | 438 us                                                 | 336 us: 1.30x faster                                              |
| coroutines              | 31.6 ms                                                | 24.5 ms: 1.29x faster                                             |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.27x faster                                              |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                            |
| sqlglot_optimize        | 65.2 ms                                                | 51.4 ms: 1.27x faster                                             |
| deepcopy_reduce         | 3.79 us                                                | 2.98 us: 1.27x faster                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                              |
| nqueens                 | 100 ms                                                 | 81.0 ms: 1.24x faster                                             |
| async_generators        | 426 ms                                                 | 347 ms: 1.23x faster                                              |
| sympy_integrate         | 24.0 ms                                                | 19.7 ms: 1.22x faster                                             |
| xml_etree_generate      | 93.8 ms                                                | 77.4 ms: 1.21x faster                                             |
| bench_thread_pool       | 946 us                                                 | 781 us: 1.21x faster                                              |
| sympy_str               | 325 ms                                                 | 270 ms: 1.21x faster                                              |
| dulwich_log             | 75.8 ms                                                | 63.0 ms: 1.20x faster                                             |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.9 ms: 1.20x faster                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                              |
| json_loads              | 28.7 us                                                | 24.3 us: 1.18x faster                                             |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                              |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.18x faster                                              |
| djangocms               | 36.9 us                                                | 31.7 us: 1.16x faster                                             |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                             |
| pickle_list             | 4.72 us                                                | 4.14 us: 1.14x faster                                             |
| json                    | 5.35 ms                                                | 4.70 ms: 1.14x faster                                             |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.14x faster                                             |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                             |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                             |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                              |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                              |
| unpickle                | 14.2 us                                                | 13.3 us: 1.07x faster                                             |
| meteor_contest          | 114 ms                                                 | 108 ms: 1.06x faster                                              |
| mdp                     | 2.74 sec                                               | 2.59 sec: 1.06x faster                                            |
| telco                   | 6.73 ms                                                | 6.45 ms: 1.04x faster                                             |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                              |
| generators              | 76.4 ms                                                | 75.7 ms: 1.01x faster                                             |
| unpickle_list           | 4.92 us                                                | 5.01 us: 1.02x slower                                             |
| pickle                  | 10.2 us                                                | 10.4 us: 1.02x slower                                             |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                              |
| gc_traversal            | 3.53 ms                                                | 3.91 ms: 1.11x slower                                             |
| python_startup_no_site  | 5.78 ms                                                | 6.47 ms: 1.12x slower                                             |
| regex_effbot            | 3.19 ms                                                | 3.62 ms: 1.13x slower                                             |
| pickle_dict             | 27.6 us                                                | 31.6 us: 1.14x slower                                             |
| coverage                | 74.7 ms                                                | 95.6 ms: 1.28x slower                                             |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
