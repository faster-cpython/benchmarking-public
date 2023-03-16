
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: d42ac00
- commit date: 2023-03-16
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.52 ms: 1.40x faster                                                        |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                       |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.39x faster                                                        |
| tornado_http   | 128 ms                                                 | 91.9 ms: 1.39x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 87.7 ms: 1.64x faster                                                        |
| float          | 109 ms                                                 | 73.7 ms: 1.48x faster                                                        |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                        |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                         |
| regex_effbot   | 3.19 ms                                                | 3.45 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 289 us: 1.57x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 203 us: 1.48x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.42 ms: 1.43x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                        |
| json_loads           | 28.7 us                                                | 24.4 us: 1.18x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 80.3 ms: 1.17x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.16 us: 1.13x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                         |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| unpickle             | 14.2 us                                                | 13.5 us: 1.05x faster                                                        |
| pickle               | 10.2 us                                                | 10.3 us: 1.01x slower                                                        |
| unpickle_list        | 4.92 us                                                | 5.00 us: 1.02x slower                                                        |
| pickle_dict          | 27.6 us                                                | 30.9 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.91 ms: 1.58x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.52 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.95 ms: 1.47x faster                                                        |
| genshi_text     | 30.6 ms                                                | 21.6 ms: 1.41x faster                                                        |
| django_template | 46.3 ms                                                | 33.4 ms: 1.39x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 47.7 ms: 1.34x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.4 ms: 2.60x faster                                                        |
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                        |
| logging_silent          | 176 ns                                                 | 95.2 ns: 1.85x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 506 ms: 1.81x faster                                                         |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.80x faster                                                         |
| richards                | 75.2 ms                                                | 43.0 ms: 1.75x faster                                                        |
| spectral_norm           | 150 ms                                                 | 90.0 ms: 1.66x faster                                                        |
| nbody                   | 144 ms                                                 | 87.7 ms: 1.64x faster                                                        |
| go                      | 226 ms                                                 | 139 ms: 1.63x faster                                                         |
| raytrace                | 467 ms                                                 | 289 ms: 1.62x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                 | 67.5 ms: 1.61x faster                                                        |
| pyflate                 | 676 ms                                                 | 425 ms: 1.59x faster                                                         |
| python_startup          | 14.1 ms                                                | 8.91 ms: 1.58x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 73.9 ms: 1.58x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 289 us: 1.57x faster                                                         |
| hexiom                  | 9.43 ms                                                | 6.11 ms: 1.54x faster                                                        |
| chaos                   | 106 ms                                                 | 68.7 ms: 1.54x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 34.0 us: 1.52x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 203 us: 1.48x faster                                                         |
| float                   | 109 ms                                                 | 73.7 ms: 1.48x faster                                                        |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.47x faster                                                         |
| mako                    | 14.7 ms                                                | 9.95 ms: 1.47x faster                                                        |
| sqlglot_parse           | 2.04 ms                                                | 1.43 ms: 1.43x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.42 ms: 1.43x faster                                                        |
| genshi_text             | 30.6 ms                                                | 21.6 ms: 1.41x faster                                                        |
| logging_simple          | 8.10 us                                                | 5.73 us: 1.41x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.41x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.52 ms: 1.40x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 42.3 ns: 1.40x faster                                                        |
| logging_format          | 8.85 us                                                | 6.32 us: 1.40x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.28 sec: 1.40x faster                                                       |
| tornado_http            | 128 ms                                                 | 91.9 ms: 1.39x faster                                                        |
| django_template         | 46.3 ms                                                | 33.4 ms: 1.39x faster                                                        |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.39x faster                                                        |
| async_tree_none         | 711 ms                                                 | 515 ms: 1.38x faster                                                         |
| coroutines              | 31.6 ms                                                | 22.9 ms: 1.38x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 691 ms: 1.38x faster                                                         |
| scimark_fft             | 421 ms                                                 | 311 ms: 1.35x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                        |
| deepcopy                | 438 us                                                 | 327 us: 1.34x faster                                                         |
| genshi_xml              | 63.7 ms                                                | 47.7 ms: 1.34x faster                                                        |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                         |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                        |
| thrift                  | 1.03 ms                                                | 780 us: 1.33x faster                                                         |
| async_tree_memoization  | 855 ms                                                 | 648 ms: 1.32x faster                                                         |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                        |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                         |
| pycparser               | 1.53 sec                                               | 1.17 sec: 1.31x faster                                                       |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.31x faster                                                         |
| deepcopy_reduce         | 3.79 us                                                | 2.92 us: 1.30x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 733 ms: 1.30x faster                                                         |
| mypy2                   | 430 ms                                                 | 333 ms: 1.29x faster                                                         |
| sqlglot_optimize        | 65.2 ms                                                | 50.9 ms: 1.28x faster                                                        |
| fannkuch                | 488 ms                                                 | 382 ms: 1.28x faster                                                         |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.41 ms: 1.24x faster                                                        |
| nqueens                 | 100 ms                                                 | 80.9 ms: 1.24x faster                                                        |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.6 ms: 1.22x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                         |
| bench_thread_pool       | 946 us                                                 | 793 us: 1.19x faster                                                         |
| dulwich_log             | 75.8 ms                                                | 63.8 ms: 1.19x faster                                                        |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                        |
| json_loads              | 28.7 us                                                | 24.4 us: 1.18x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 80.3 ms: 1.17x faster                                                        |
| sympy_expand            | 534 ms                                                 | 460 ms: 1.16x faster                                                         |
| json                    | 5.35 ms                                                | 4.62 ms: 1.16x faster                                                        |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                                         |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                        |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                        |
| pickle_list             | 4.72 us                                                | 4.16 us: 1.13x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.47 sec: 1.11x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                         |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.11x faster                                                         |
| sqlite_synth            | 2.92 us                                                | 2.65 us: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                         |
| unpickle                | 14.2 us                                                | 13.5 us: 1.05x faster                                                        |
| telco                   | 6.73 ms                                                | 6.52 ms: 1.03x faster                                                        |
| async_generators        | 426 ms                                                 | 414 ms: 1.03x faster                                                         |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                         |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                         |
| pickle                  | 10.2 us                                                | 10.3 us: 1.01x slower                                                        |
| unpickle_list           | 4.92 us                                                | 5.00 us: 1.02x slower                                                        |
| gc_traversal            | 3.53 ms                                                | 3.66 ms: 1.04x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.45 ms: 1.08x slower                                                        |
| pickle_dict             | 27.6 us                                                | 30.9 us: 1.12x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.52 ms: 1.13x slower                                                        |
| dask                    | 436 ms                                                 | 510 ms: 1.17x slower                                                         |
| coverage                | 74.7 ms                                                | 97.2 ms: 1.30x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230316-3.12.0a6+-d42ac00/bm-20230316-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a6+-d42ac00.json: comprehensions
