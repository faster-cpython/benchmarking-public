
# Results vs. 3.10.4

- fork: brandtbucher
- ref: de_epfreeze
- machine: linux-x86_64
- commit hash: 034e2bf
- commit date: 2023-03-16
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.32x faster                                                |
| chameleon      | 9.17 ms                                                | 6.43 ms: 1.43x faster                                               |
| docutils       | 3.18 sec                                               | 2.53 sec: 1.25x faster                                              |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                               |
| tornado_http   | 128 ms                                                 | 91.7 ms: 1.40x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 89.3 ms: 1.61x faster                                               |
| float          | 109 ms                                                 | 73.6 ms: 1.48x faster                                               |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.32x faster                                                |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                                |
| regex_v8       | 25.0 ms                                                | 25.6 ms: 1.02x slower                                               |
| regex_effbot   | 3.19 ms                                                | 3.42 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                                |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.51x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.41 ms: 1.43x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 56.3 ms: 1.32x faster                                               |
| json_loads           | 28.7 us                                                | 24.4 us: 1.18x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 81.7 ms: 1.15x faster                                               |
| pickle_list          | 4.72 us                                                | 4.16 us: 1.13x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                |
| unpickle             | 14.2 us                                                | 13.7 us: 1.04x faster                                               |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                               |
| unpickle_list        | 4.92 us                                                | 5.19 us: 1.05x slower                                               |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.50 ms: 1.48x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.47 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.2 ms: 1.43x faster                                               |
| genshi_text     | 30.6 ms                                                | 21.7 ms: 1.41x faster                                               |
| django_template | 46.3 ms                                                | 33.2 ms: 1.40x faster                                               |
| genshi_xml      | 63.7 ms                                                | 48.4 ms: 1.32x faster                                               |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.1 ms: 2.54x faster                                               |
| deltablue               | 7.28 ms                                                | 3.16 ms: 2.30x faster                                               |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                |
| logging_silent          | 176 ns                                                 | 96.1 ns: 1.83x faster                                               |
| asyncio_tcp             | 914 ms                                                 | 508 ms: 1.80x faster                                                |
| richards                | 75.2 ms                                                | 43.9 ms: 1.71x faster                                               |
| spectral_norm           | 150 ms                                                 | 90.3 ms: 1.66x faster                                               |
| go                      | 226 ms                                                 | 137 ms: 1.65x faster                                                |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 66.8 ms: 1.63x faster                                               |
| nbody                   | 144 ms                                                 | 89.3 ms: 1.61x faster                                               |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                                |
| pyflate                 | 676 ms                                                 | 423 ms: 1.60x faster                                                |
| crypto_pyaes            | 117 ms                                                 | 74.2 ms: 1.57x faster                                               |
| chaos                   | 106 ms                                                 | 67.2 ms: 1.57x faster                                               |
| hexiom                  | 9.43 ms                                                | 6.10 ms: 1.55x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.51x faster                                                |
| deepcopy_memo           | 51.7 us                                                | 34.2 us: 1.51x faster                                               |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                                |
| python_startup          | 14.1 ms                                                | 9.50 ms: 1.48x faster                                               |
| float                   | 109 ms                                                 | 73.6 ms: 1.48x faster                                               |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                               |
| coroutines              | 31.6 ms                                                | 22.0 ms: 1.44x faster                                               |
| mako                    | 14.7 ms                                                | 10.2 ms: 1.43x faster                                               |
| json_dumps              | 13.4 ms                                                | 9.41 ms: 1.43x faster                                               |
| chameleon               | 9.17 ms                                                | 6.43 ms: 1.43x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                              |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.41x faster                                               |
| genshi_text             | 30.6 ms                                                | 21.7 ms: 1.41x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 609 ms: 1.40x faster                                                |
| unpack_sequence         | 59.4 ns                                                | 42.4 ns: 1.40x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.40x faster                                               |
| tornado_http            | 128 ms                                                 | 91.7 ms: 1.40x faster                                               |
| django_template         | 46.3 ms                                                | 33.2 ms: 1.40x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 685 ms: 1.39x faster                                                |
| logging_simple          | 8.10 us                                                | 5.88 us: 1.38x faster                                               |
| scimark_fft             | 421 ms                                                 | 306 ms: 1.38x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                              |
| logging_format          | 8.85 us                                                | 6.54 us: 1.35x faster                                               |
| thrift                  | 1.03 ms                                                | 774 us: 1.34x faster                                                |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                               |
| 2to3                    | 335 ms                                                 | 253 ms: 1.32x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 56.3 ms: 1.32x faster                                               |
| deepcopy                | 438 us                                                 | 332 us: 1.32x faster                                                |
| async_tree_none         | 711 ms                                                 | 539 ms: 1.32x faster                                                |
| genshi_xml              | 63.7 ms                                                | 48.4 ms: 1.32x faster                                               |
| regex_compile           | 177 ms                                                 | 135 ms: 1.32x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.32x faster                                               |
| pycparser               | 1.53 sec                                               | 1.17 sec: 1.31x faster                                              |
| fannkuch                | 488 ms                                                 | 377 ms: 1.29x faster                                                |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                |
| deepcopy_reduce         | 3.79 us                                                | 2.97 us: 1.27x faster                                               |
| sqlglot_optimize        | 65.2 ms                                                | 51.7 ms: 1.26x faster                                               |
| docutils                | 3.18 sec                                               | 2.53 sec: 1.25x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.39 ms: 1.24x faster                                               |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.6 ms: 1.22x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 135 ms: 1.22x faster                                                |
| nqueens                 | 100 ms                                                 | 82.3 ms: 1.22x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 782 ms: 1.21x faster                                                |
| dulwich_log             | 75.8 ms                                                | 62.6 ms: 1.21x faster                                               |
| bench_thread_pool       | 946 us                                                 | 796 us: 1.19x faster                                                |
| json_loads              | 28.7 us                                                | 24.4 us: 1.18x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 20.5 ms: 1.17x faster                                               |
| xml_etree_generate      | 93.8 ms                                                | 81.7 ms: 1.15x faster                                               |
| mdp                     | 2.74 sec                                               | 2.39 sec: 1.15x faster                                              |
| sympy_expand            | 534 ms                                                 | 467 ms: 1.14x faster                                                |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                               |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                               |
| sympy_str               | 325 ms                                                 | 285 ms: 1.14x faster                                                |
| pickle_list             | 4.72 us                                                | 4.16 us: 1.13x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                |
| sqlite_synth            | 2.92 us                                                | 2.64 us: 1.11x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.49 ms: 1.11x faster                                               |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                                |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                                |
| unpickle                | 14.2 us                                                | 13.7 us: 1.04x faster                                               |
| async_generators        | 426 ms                                                 | 416 ms: 1.03x faster                                                |
| telco                   | 6.73 ms                                                | 6.58 ms: 1.02x faster                                               |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                |
| gc_traversal            | 3.53 ms                                                | 3.55 ms: 1.01x slower                                               |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                               |
| regex_v8                | 25.0 ms                                                | 25.6 ms: 1.02x slower                                               |
| unpickle_list           | 4.92 us                                                | 5.19 us: 1.05x slower                                               |
| regex_effbot            | 3.19 ms                                                | 3.42 ms: 1.07x slower                                               |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.47 ms: 1.12x slower                                               |
| dask                    | 436 ms                                                 | 511 ms: 1.17x slower                                                |
| coverage                | 74.7 ms                                                | 90.3 ms: 1.21x slower                                               |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230316-3.12.0a6+-034e2bf/bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf.json: comprehensions
