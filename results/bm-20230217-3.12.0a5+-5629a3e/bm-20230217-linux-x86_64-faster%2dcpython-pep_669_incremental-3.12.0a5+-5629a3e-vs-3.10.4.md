
# Results vs. 3.10.4

- fork: faster-cpython
- ref: pep_669_incremental
- machine: linux-x86_64
- commit hash: 5629a3e
- commit date: 2023-02-17
- overall geometric mean: 1.32x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 244 ms: 1.37x faster                                                            |
| chameleon      | 9.17 ms                                                | 6.33 ms: 1.45x faster                                                           |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                          |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                           |
| tornado_http   | 128 ms                                                 | 93.3 ms: 1.37x faster                                                           |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.4 ms: 1.56x faster                                                           |
| float          | 109 ms                                                 | 72.4 ms: 1.51x faster                                                           |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 125 ms: 1.42x faster                                                            |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                           |
| regex_dna      | 214 ms                                                 | 205 ms: 1.04x faster                                                            |
| regex_effbot   | 3.19 ms                                                | 3.65 ms: 1.14x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 279 us: 1.62x faster                                                            |
| unpickle_pure_python | 302 us                                                 | 193 us: 1.56x faster                                                            |
| json_dumps           | 13.4 ms                                                | 9.37 ms: 1.43x faster                                                           |
| xml_etree_process    | 74.5 ms                                                | 55.0 ms: 1.36x faster                                                           |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                                           |
| xml_etree_generate   | 93.8 ms                                                | 80.3 ms: 1.17x faster                                                           |
| pickle_list          | 4.72 us                                                | 4.25 us: 1.11x faster                                                           |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                            |
| unpickle             | 14.2 us                                                | 13.7 us: 1.03x faster                                                           |
| pickle               | 10.2 us                                                | 10.3 us: 1.02x slower                                                           |
| unpickle_list        | 4.92 us                                                | 5.08 us: 1.03x slower                                                           |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.97 ms: 1.57x faster                                                           |
| python_startup_no_site | 5.78 ms                                                | 6.52 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.76 ms: 1.50x faster                                                           |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.49x faster                                                           |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                           |
| genshi_xml      | 63.7 ms                                                | 46.0 ms: 1.39x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230217-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-5629a3e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.8 ms: 2.48x faster                                                           |
| deltablue               | 7.28 ms                                                | 3.13 ms: 2.33x faster                                                           |
| logging_silent          | 176 ns                                                 | 93.8 ns: 1.88x faster                                                           |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                            |
| asyncio_tcp             | 914 ms                                                 | 501 ms: 1.82x faster                                                            |
| richards                | 75.2 ms                                                | 41.9 ms: 1.80x faster                                                           |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                                            |
| pyflate                 | 676 ms                                                 | 401 ms: 1.69x faster                                                            |
| raytrace                | 467 ms                                                 | 280 ms: 1.66x faster                                                            |
| scimark_monte_carlo     | 109 ms                                                 | 65.2 ms: 1.66x faster                                                           |
| chaos                   | 106 ms                                                 | 64.5 ms: 1.64x faster                                                           |
| pickle_pure_python      | 452 us                                                 | 279 us: 1.62x faster                                                            |
| spectral_norm           | 150 ms                                                 | 92.7 ms: 1.61x faster                                                           |
| crypto_pyaes            | 117 ms                                                 | 72.6 ms: 1.61x faster                                                           |
| hexiom                  | 9.43 ms                                                | 5.99 ms: 1.57x faster                                                           |
| python_startup          | 14.1 ms                                                | 8.97 ms: 1.57x faster                                                           |
| unpickle_pure_python    | 302 us                                                 | 193 us: 1.56x faster                                                            |
| nbody                   | 144 ms                                                 | 92.4 ms: 1.56x faster                                                           |
| deepcopy_memo           | 51.7 us                                                | 33.4 us: 1.55x faster                                                           |
| float                   | 109 ms                                                 | 72.4 ms: 1.51x faster                                                           |
| coroutines              | 31.6 ms                                                | 21.1 ms: 1.50x faster                                                           |
| mako                    | 14.7 ms                                                | 9.76 ms: 1.50x faster                                                           |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                            |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.49x faster                                                           |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                           |
| chameleon               | 9.17 ms                                                | 6.33 ms: 1.45x faster                                                           |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                          |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                           |
| json_dumps              | 13.4 ms                                                | 9.37 ms: 1.43x faster                                                           |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.43x faster                                                           |
| pprint_safe_repr        | 953 ms                                                 | 671 ms: 1.42x faster                                                            |
| regex_compile           | 177 ms                                                 | 125 ms: 1.42x faster                                                            |
| logging_simple          | 8.10 us                                                | 5.72 us: 1.42x faster                                                           |
| unpack_sequence         | 59.4 ns                                                | 42.4 ns: 1.40x faster                                                           |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                           |
| logging_format          | 8.85 us                                                | 6.33 us: 1.40x faster                                                           |
| genshi_xml              | 63.7 ms                                                | 46.0 ms: 1.39x faster                                                           |
| scimark_fft             | 421 ms                                                 | 305 ms: 1.38x faster                                                            |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                          |
| 2to3                    | 335 ms                                                 | 244 ms: 1.37x faster                                                            |
| async_tree_none         | 711 ms                                                 | 518 ms: 1.37x faster                                                            |
| tornado_http            | 128 ms                                                 | 93.3 ms: 1.37x faster                                                           |
| fannkuch                | 488 ms                                                 | 356 ms: 1.37x faster                                                            |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                                            |
| xml_etree_process       | 74.5 ms                                                | 55.0 ms: 1.36x faster                                                           |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.35x faster                                                          |
| deepcopy                | 438 us                                                 | 325 us: 1.35x faster                                                            |
| gunicorn                | 1.43 ms                                                | 1.06 ms: 1.34x faster                                                           |
| aiohttp                 | 1.34 ms                                                | 1000 us: 1.34x faster                                                           |
| mypy2                   | 430 ms                                                 | 325 ms: 1.32x faster                                                            |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.31x faster                                                           |
| async_tree_memoization  | 855 ms                                                 | 655 ms: 1.31x faster                                                            |
| nqueens                 | 100 ms                                                 | 76.9 ms: 1.30x faster                                                           |
| sqlglot_normalize       | 134 ms                                                 | 103 ms: 1.30x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.20 ms: 1.30x faster                                                           |
| sqlglot_optimize        | 65.2 ms                                                | 50.6 ms: 1.29x faster                                                           |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                                          |
| async_tree_cpu_io_mixed | 949 ms                                                 | 750 ms: 1.26x faster                                                            |
| dulwich_log             | 75.8 ms                                                | 61.2 ms: 1.24x faster                                                           |
| sympy_integrate         | 24.0 ms                                                | 19.5 ms: 1.23x faster                                                           |
| sqlalchemy_declarative  | 165 ms                                                 | 135 ms: 1.23x faster                                                            |
| sympy_str               | 325 ms                                                 | 265 ms: 1.22x faster                                                            |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.6 ms: 1.22x faster                                                           |
| bench_thread_pool       | 946 us                                                 | 779 us: 1.21x faster                                                            |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                                           |
| sympy_expand            | 534 ms                                                 | 449 ms: 1.19x faster                                                            |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                            |
| xml_etree_generate      | 93.8 ms                                                | 80.3 ms: 1.17x faster                                                           |
| json                    | 5.35 ms                                                | 4.62 ms: 1.16x faster                                                           |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                                           |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                           |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                           |
| mdp                     | 2.74 sec                                               | 2.46 sec: 1.12x faster                                                          |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                           |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.11x faster                                                            |
| pickle_list             | 4.72 us                                                | 4.25 us: 1.11x faster                                                           |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                            |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                           |
| telco                   | 6.73 ms                                                | 6.38 ms: 1.05x faster                                                           |
| regex_dna               | 214 ms                                                 | 205 ms: 1.04x faster                                                            |
| unpickle                | 14.2 us                                                | 13.7 us: 1.03x faster                                                           |
| async_generators        | 426 ms                                                 | 422 ms: 1.01x faster                                                            |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                            |
| pickle                  | 10.2 us                                                | 10.3 us: 1.02x slower                                                           |
| gc_traversal            | 3.53 ms                                                | 3.59 ms: 1.02x slower                                                           |
| unpickle_list           | 4.92 us                                                | 5.08 us: 1.03x slower                                                           |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                                           |
| python_startup_no_site  | 5.78 ms                                                | 6.52 ms: 1.13x slower                                                           |
| regex_effbot            | 3.19 ms                                                | 3.65 ms: 1.14x slower                                                           |
| coverage                | 74.7 ms                                                | 99.2 ms: 1.33x slower                                                           |
| Geometric mean          | (ref)                                                  | 1.32x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
