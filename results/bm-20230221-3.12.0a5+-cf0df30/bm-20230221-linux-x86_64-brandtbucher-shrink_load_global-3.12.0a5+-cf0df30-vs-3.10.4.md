
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_load_global
- machine: linux-x86_64
- commit hash: cf0df30
- commit date: 2023-02-21
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.35x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.38 ms: 1.44x faster                                                      |
| docutils       | 3.18 sec                                               | 2.60 sec: 1.22x faster                                                     |
| html5lib       | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                      |
| tornado_http   | 128 ms                                                 | 94.5 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.2 ms: 1.53x faster                                                      |
| float          | 109 ms                                                 | 72.3 ms: 1.51x faster                                                      |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 128 ms: 1.39x faster                                                       |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                      |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                                       |
| regex_effbot   | 3.19 ms                                                | 3.63 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 54.5 ms: 1.37x faster                                                      |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 80.0 ms: 1.17x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.13 us: 1.14x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                       |
| unpickle_list        | 4.92 us                                                | 5.03 us: 1.02x slower                                                      |
| pickle_dict          | 27.6 us                                                | 30.4 us: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.01 ms: 1.56x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.49x faster                                                      |
| mako            | 14.7 ms                                                | 9.99 ms: 1.47x faster                                                      |
| django_template | 46.3 ms                                                | 33.3 ms: 1.39x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 46.5 ms: 1.37x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230221-linux-x86_64-brandtbucher-shrink_load_global-3.12.0a5+-cf0df30 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.9 ms: 2.56x faster                                                      |
| deltablue               | 7.28 ms                                                | 3.13 ms: 2.32x faster                                                      |
| logging_silent          | 176 ns                                                 | 91.0 ns: 1.94x faster                                                      |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                       |
| asyncio_tcp             | 914 ms                                                 | 502 ms: 1.82x faster                                                       |
| richards                | 75.2 ms                                                | 42.6 ms: 1.77x faster                                                      |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                                       |
| pyflate                 | 676 ms                                                 | 401 ms: 1.68x faster                                                       |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                 | 66.9 ms: 1.62x faster                                                      |
| crypto_pyaes            | 117 ms                                                 | 72.3 ms: 1.61x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                                       |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.59x faster                                                      |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.58x faster                                                      |
| python_startup          | 14.1 ms                                                | 9.01 ms: 1.56x faster                                                      |
| hexiom                  | 9.43 ms                                                | 6.03 ms: 1.56x faster                                                      |
| nbody                   | 144 ms                                                 | 94.2 ms: 1.53x faster                                                      |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                       |
| float                   | 109 ms                                                 | 72.3 ms: 1.51x faster                                                      |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.49x faster                                                      |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.48x faster                                                       |
| deepcopy_memo           | 51.7 us                                                | 35.2 us: 1.47x faster                                                      |
| mako                    | 14.7 ms                                                | 9.99 ms: 1.47x faster                                                      |
| coroutines              | 31.6 ms                                                | 21.9 ms: 1.44x faster                                                      |
| chameleon               | 9.17 ms                                                | 6.38 ms: 1.44x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                                      |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                     |
| json_dumps              | 13.4 ms                                                | 9.40 ms: 1.43x faster                                                      |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                      |
| logging_format          | 8.85 us                                                | 6.26 us: 1.41x faster                                                      |
| pprint_safe_repr        | 953 ms                                                 | 675 ms: 1.41x faster                                                       |
| logging_simple          | 8.10 us                                                | 5.75 us: 1.41x faster                                                      |
| html5lib                | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                      |
| async_tree_memoization  | 855 ms                                                 | 610 ms: 1.40x faster                                                       |
| django_template         | 46.3 ms                                                | 33.3 ms: 1.39x faster                                                      |
| regex_compile           | 177 ms                                                 | 128 ms: 1.39x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                     |
| genshi_xml              | 63.7 ms                                                | 46.5 ms: 1.37x faster                                                      |
| xml_etree_process       | 74.5 ms                                                | 54.5 ms: 1.37x faster                                                      |
| async_tree_none         | 711 ms                                                 | 521 ms: 1.36x faster                                                       |
| thrift                  | 1.03 ms                                                | 760 us: 1.36x faster                                                       |
| fannkuch                | 488 ms                                                 | 359 ms: 1.36x faster                                                       |
| tornado_http            | 128 ms                                                 | 94.5 ms: 1.36x faster                                                      |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.03 ms: 1.35x faster                                                      |
| 2to3                    | 335 ms                                                 | 248 ms: 1.35x faster                                                       |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                       |
| pycparser               | 1.53 sec                                               | 1.14 sec: 1.35x faster                                                     |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                      |
| unpack_sequence         | 59.4 ns                                                | 44.7 ns: 1.33x faster                                                      |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                      |
| deepcopy                | 438 us                                                 | 333 us: 1.31x faster                                                       |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.31x faster                                                       |
| mypy2                   | 430 ms                                                 | 331 ms: 1.30x faster                                                       |
| nqueens                 | 100 ms                                                 | 77.5 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 735 ms: 1.29x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 50.7 ms: 1.29x faster                                                      |
| deepcopy_reduce         | 3.79 us                                                | 2.98 us: 1.27x faster                                                      |
| docutils                | 3.18 sec                                               | 2.60 sec: 1.22x faster                                                     |
| dulwich_log             | 75.8 ms                                                | 63.0 ms: 1.20x faster                                                      |
| bench_thread_pool       | 946 us                                                 | 788 us: 1.20x faster                                                       |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.9 ms: 1.20x faster                                                      |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                       |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                                      |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.19x faster                                                      |
| sympy_expand            | 534 ms                                                 | 452 ms: 1.18x faster                                                       |
| xml_etree_generate      | 93.8 ms                                                | 80.0 ms: 1.17x faster                                                      |
| json                    | 5.35 ms                                                | 4.58 ms: 1.17x faster                                                      |
| sympy_str               | 325 ms                                                 | 281 ms: 1.15x faster                                                       |
| pickle_list             | 4.72 us                                                | 4.13 us: 1.14x faster                                                      |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.45 sec: 1.12x faster                                                     |
| sqlite_synth            | 2.92 us                                                | 2.62 us: 1.12x faster                                                      |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                      |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                      |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                       |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.11x faster                                                       |
| create_gc_cycles        | 1.65 ms                                                | 1.49 ms: 1.10x faster                                                      |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                       |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                       |
| telco                   | 6.73 ms                                                | 6.42 ms: 1.05x faster                                                      |
| async_generators        | 426 ms                                                 | 407 ms: 1.05x faster                                                       |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                                       |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                       |
| unpickle_list           | 4.92 us                                                | 5.03 us: 1.02x slower                                                      |
| gc_traversal            | 3.53 ms                                                | 3.61 ms: 1.02x slower                                                      |
| pickle_dict             | 27.6 us                                                | 30.4 us: 1.10x slower                                                      |
| python_startup_no_site  | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.63 ms: 1.14x slower                                                      |
| dask                    | 436 ms                                                 | 497 ms: 1.14x slower                                                       |
| coverage                | 74.7 ms                                                | 97.2 ms: 1.30x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                               |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
