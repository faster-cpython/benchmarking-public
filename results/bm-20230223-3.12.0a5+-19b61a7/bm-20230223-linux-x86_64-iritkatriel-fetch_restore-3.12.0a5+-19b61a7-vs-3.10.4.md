
# Results vs. 3.10.4

- fork: iritkatriel
- ref: fetch_restore
- machine: linux-x86_64
- commit hash: 19b61a7
- commit date: 2023-02-23
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                 |
| chameleon      | 9.17 ms                                                | 6.48 ms: 1.41x faster                                                |
| docutils       | 3.18 sec                                               | 2.55 sec: 1.24x faster                                               |
| html5lib       | 85.9 ms                                                | 62.4 ms: 1.38x faster                                                |
| tornado_http   | 128 ms                                                 | 95.3 ms: 1.34x faster                                                |
| Geometric mean | (ref)                                                  | 1.34x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.6 ms: 1.54x faster                                                |
| float          | 109 ms                                                 | 73.5 ms: 1.48x faster                                                |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                 |
| regex_v8       | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                 |
| regex_effbot   | 3.19 ms                                                | 3.27 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 293 us: 1.54x faster                                                 |
| unpickle_pure_python | 302 us                                                 | 203 us: 1.49x faster                                                 |
| json_dumps           | 13.4 ms                                                | 9.34 ms: 1.44x faster                                                |
| xml_etree_process    | 74.5 ms                                                | 55.8 ms: 1.34x faster                                                |
| json_loads           | 28.7 us                                                | 23.8 us: 1.20x faster                                                |
| pickle_list          | 4.72 us                                                | 3.92 us: 1.20x faster                                                |
| xml_etree_generate   | 93.8 ms                                                | 81.5 ms: 1.15x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 98.5 ms: 1.13x faster                                                |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                 |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                                |
| pickle               | 10.2 us                                                | 9.95 us: 1.02x faster                                                |
| pickle_dict          | 27.6 us                                                | 30.1 us: 1.09x slower                                                |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                         |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.97 ms: 1.57x faster                                                |
| python_startup_no_site | 5.78 ms                                                | 6.51 ms: 1.13x slower                                                |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.93 ms: 1.48x faster                                                |
| genshi_text     | 30.6 ms                                                | 21.5 ms: 1.42x faster                                                |
| django_template | 46.3 ms                                                | 33.5 ms: 1.38x faster                                                |
| genshi_xml      | 63.7 ms                                                | 48.1 ms: 1.32x faster                                                |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                         |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-19b61a7 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.5 ms: 2.50x faster                                                |
| deltablue               | 7.28 ms                                                | 3.24 ms: 2.25x faster                                                |
| logging_silent          | 176 ns                                                 | 95.4 ns: 1.85x faster                                                |
| asyncio_tcp             | 914 ms                                                 | 505 ms: 1.81x faster                                                 |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                                 |
| richards                | 75.2 ms                                                | 43.4 ms: 1.73x faster                                                |
| go                      | 226 ms                                                 | 136 ms: 1.66x faster                                                 |
| pyflate                 | 676 ms                                                 | 411 ms: 1.65x faster                                                 |
| scimark_monte_carlo     | 109 ms                                                 | 66.2 ms: 1.64x faster                                                |
| raytrace                | 467 ms                                                 | 289 ms: 1.61x faster                                                 |
| crypto_pyaes            | 117 ms                                                 | 73.8 ms: 1.58x faster                                                |
| python_startup          | 14.1 ms                                                | 8.97 ms: 1.57x faster                                                |
| spectral_norm           | 150 ms                                                 | 95.9 ms: 1.56x faster                                                |
| pickle_pure_python      | 452 us                                                 | 293 us: 1.54x faster                                                 |
| chaos                   | 106 ms                                                 | 68.5 ms: 1.54x faster                                                |
| nbody                   | 144 ms                                                 | 93.6 ms: 1.54x faster                                                |
| hexiom                  | 9.43 ms                                                | 6.22 ms: 1.52x faster                                                |
| unpickle_pure_python    | 302 us                                                 | 203 us: 1.49x faster                                                 |
| float                   | 109 ms                                                 | 73.5 ms: 1.48x faster                                                |
| mako                    | 14.7 ms                                                | 9.93 ms: 1.48x faster                                                |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                 |
| deepcopy_memo           | 51.7 us                                                | 35.6 us: 1.45x faster                                                |
| json_dumps              | 13.4 ms                                                | 9.34 ms: 1.44x faster                                                |
| genshi_text             | 30.6 ms                                                | 21.5 ms: 1.42x faster                                                |
| unpack_sequence         | 59.4 ns                                                | 41.9 ns: 1.42x faster                                                |
| coroutines              | 31.6 ms                                                | 22.3 ms: 1.42x faster                                                |
| chameleon               | 9.17 ms                                                | 6.48 ms: 1.41x faster                                                |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.41x faster                                                |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.39x faster                                                |
| pprint_safe_repr        | 953 ms                                                 | 686 ms: 1.39x faster                                                 |
| django_template         | 46.3 ms                                                | 33.5 ms: 1.38x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                               |
| html5lib                | 85.9 ms                                                | 62.4 ms: 1.38x faster                                                |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.37x faster                                               |
| logging_simple          | 8.10 us                                                | 5.93 us: 1.36x faster                                                |
| async_tree_none         | 711 ms                                                 | 522 ms: 1.36x faster                                                 |
| logging_format          | 8.85 us                                                | 6.51 us: 1.36x faster                                                |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                 |
| tornado_http            | 128 ms                                                 | 95.3 ms: 1.34x faster                                                |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                 |
| xml_etree_process       | 74.5 ms                                                | 55.8 ms: 1.34x faster                                                |
| fannkuch                | 488 ms                                                 | 367 ms: 1.33x faster                                                 |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                 |
| thrift                  | 1.03 ms                                                | 779 us: 1.33x faster                                                 |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                |
| genshi_xml              | 63.7 ms                                                | 48.1 ms: 1.32x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                |
| async_tree_memoization  | 855 ms                                                 | 662 ms: 1.29x faster                                                 |
| mypy2                   | 430 ms                                                 | 334 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed | 949 ms                                                 | 738 ms: 1.29x faster                                                 |
| deepcopy                | 438 us                                                 | 341 us: 1.28x faster                                                 |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                 |
| sqlglot_optimize        | 65.2 ms                                                | 51.2 ms: 1.27x faster                                                |
| docutils                | 3.18 sec                                               | 2.55 sec: 1.24x faster                                               |
| deepcopy_reduce         | 3.79 us                                                | 3.08 us: 1.23x faster                                                |
| nqueens                 | 100 ms                                                 | 81.6 ms: 1.23x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.51 ms: 1.21x faster                                                |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                 |
| json_loads              | 28.7 us                                                | 23.8 us: 1.20x faster                                                |
| pickle_list             | 4.72 us                                                | 3.92 us: 1.20x faster                                                |
| dulwich_log             | 75.8 ms                                                | 63.3 ms: 1.20x faster                                                |
| bench_thread_pool       | 946 us                                                 | 794 us: 1.19x faster                                                 |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.2 ms: 1.18x faster                                                |
| json                    | 5.35 ms                                                | 4.55 ms: 1.18x faster                                                |
| sympy_integrate         | 24.0 ms                                                | 20.7 ms: 1.16x faster                                                |
| xml_etree_generate      | 93.8 ms                                                | 81.5 ms: 1.15x faster                                                |
| sympy_expand            | 534 ms                                                 | 465 ms: 1.15x faster                                                 |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                                |
| regex_v8                | 25.0 ms                                                | 22.1 ms: 1.13x faster                                                |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                                |
| sympy_str               | 325 ms                                                 | 287 ms: 1.13x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                 | 98.5 ms: 1.13x faster                                                |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.13x faster                                                |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.12x faster                                                |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                 |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                                 |
| mdp                     | 2.74 sec                                               | 2.53 sec: 1.08x faster                                               |
| telco                   | 6.73 ms                                                | 6.42 ms: 1.05x faster                                                |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                                |
| async_generators        | 426 ms                                                 | 411 ms: 1.04x faster                                                 |
| pickle                  | 10.2 us                                                | 9.95 us: 1.02x faster                                                |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                 |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                 |
| regex_effbot            | 3.19 ms                                                | 3.27 ms: 1.02x slower                                                |
| pickle_dict             | 27.6 us                                                | 30.1 us: 1.09x slower                                                |
| python_startup_no_site  | 5.78 ms                                                | 6.51 ms: 1.13x slower                                                |
| gc_traversal            | 3.53 ms                                                | 4.07 ms: 1.15x slower                                                |
| dask                    | 436 ms                                                 | 509 ms: 1.17x slower                                                 |
| coverage                | 74.7 ms                                                | 95.9 ms: 1.28x slower                                                |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                         |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
