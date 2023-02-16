
# Results vs. 3.10.4

- fork: python
- ref: e5bd5ad70d9e549eeb80
- machine: linux-x86_64
- commit hash: e5bd5ad
- commit date: 2023-01-13
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.33x faster                                                   |
| chameleon      | 9.17 ms                                                | 6.25 ms: 1.47x faster                                                  |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                 |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                  |
| tornado_http   | 128 ms                                                 | 93.2 ms: 1.38x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 109 ms                                                 | 71.7 ms: 1.52x faster                                                  |
| nbody          | 144 ms                                                 | 97.0 ms: 1.48x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                  |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                                   |
| regex_effbot   | 3.19 ms                                                | 3.43 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 281 us: 1.61x faster                                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                   |
| json_dumps           | 13.4 ms                                                | 9.35 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.40x faster                                                  |
| xml_etree_generate   | 93.8 ms                                                | 76.3 ms: 1.23x faster                                                  |
| pickle_list          | 4.72 us                                                | 3.99 us: 1.18x faster                                                  |
| json_loads           | 28.7 us                                                | 24.4 us: 1.18x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                                   |
| pickle               | 10.2 us                                                | 9.86 us: 1.03x faster                                                  |
| unpickle_list        | 4.92 us                                                | 4.88 us: 1.01x faster                                                  |
| pickle_dict          | 27.6 us                                                | 30.0 us: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.54 ms: 1.65x faster                                                  |
| python_startup_no_site | 5.78 ms                                                | 6.11 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.71 ms: 1.51x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                  |
| django_template | 46.3 ms                                                | 31.9 ms: 1.45x faster                                                  |
| genshi_xml      | 63.7 ms                                                | 46.6 ms: 1.37x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.17 ms: 2.30x faster                                                  |
| logging_silent          | 176 ns                                                 | 89.4 ns: 1.97x faster                                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                   |
| richards                | 75.2 ms                                                | 41.2 ms: 1.83x faster                                                  |
| asyncio_tcp             | 914 ms                                                 | 505 ms: 1.81x faster                                                   |
| scimark_monte_carlo     | 109 ms                                                 | 64.3 ms: 1.69x faster                                                  |
| pyflate                 | 676 ms                                                 | 401 ms: 1.69x faster                                                   |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                   |
| raytrace                | 467 ms                                                 | 279 ms: 1.67x faster                                                   |
| python_startup          | 14.1 ms                                                | 8.54 ms: 1.65x faster                                                  |
| pickle_pure_python      | 452 us                                                 | 281 us: 1.61x faster                                                   |
| spectral_norm           | 150 ms                                                 | 94.5 ms: 1.58x faster                                                  |
| hexiom                  | 9.43 ms                                                | 6.03 ms: 1.56x faster                                                  |
| crypto_pyaes            | 117 ms                                                 | 74.8 ms: 1.56x faster                                                  |
| chaos                   | 106 ms                                                 | 68.0 ms: 1.55x faster                                                  |
| deepcopy_memo           | 51.7 us                                                | 33.7 us: 1.53x faster                                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                   |
| float                   | 109 ms                                                 | 71.7 ms: 1.52x faster                                                  |
| mako                    | 14.7 ms                                                | 9.71 ms: 1.51x faster                                                  |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                                   |
| nbody                   | 144 ms                                                 | 97.0 ms: 1.48x faster                                                  |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                  |
| chameleon               | 9.17 ms                                                | 6.25 ms: 1.47x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                  |
| django_template         | 46.3 ms                                                | 31.9 ms: 1.45x faster                                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.68 ms: 1.45x faster                                                  |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                 |
| json_dumps              | 13.4 ms                                                | 9.35 ms: 1.44x faster                                                  |
| pprint_safe_repr        | 953 ms                                                 | 663 ms: 1.44x faster                                                   |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                  |
| logging_simple          | 8.10 us                                                | 5.66 us: 1.43x faster                                                  |
| logging_format          | 8.85 us                                                | 6.22 us: 1.42x faster                                                  |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                                 |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.40x faster                                                  |
| async_tree_memoization  | 855 ms                                                 | 617 ms: 1.39x faster                                                   |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                                   |
| tornado_http            | 128 ms                                                 | 93.2 ms: 1.38x faster                                                  |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| genshi_xml              | 63.7 ms                                                | 46.6 ms: 1.37x faster                                                  |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                 |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                   |
| aiohttp                 | 1.34 ms                                                | 997 us: 1.34x faster                                                   |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                  |
| 2to3                    | 335 ms                                                 | 251 ms: 1.33x faster                                                   |
| unpack_sequence         | 59.4 ns                                                | 44.5 ns: 1.33x faster                                                  |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                                   |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.91 us: 1.30x faster                                                  |
| sqlglot_optimize        | 65.2 ms                                                | 50.6 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 737 ms: 1.29x faster                                                   |
| nqueens                 | 100 ms                                                 | 77.8 ms: 1.29x faster                                                  |
| coroutines              | 31.6 ms                                                | 24.6 ms: 1.28x faster                                                  |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                 |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                   |
| xml_etree_generate      | 93.8 ms                                                | 76.3 ms: 1.23x faster                                                  |
| dulwich_log             | 75.8 ms                                                | 62.2 ms: 1.22x faster                                                  |
| bench_thread_pool       | 946 us                                                 | 778 us: 1.22x faster                                                   |
| async_generators        | 426 ms                                                 | 351 ms: 1.22x faster                                                   |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.19x faster                                                  |
| pickle_list             | 4.72 us                                                | 3.99 us: 1.18x faster                                                  |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.18x faster                                                   |
| json_loads              | 28.7 us                                                | 24.4 us: 1.18x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.16x faster                                                  |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                                   |
| create_gc_cycles        | 1.65 ms                                                | 1.44 ms: 1.15x faster                                                  |
| djangocms               | 36.9 us                                                | 32.2 us: 1.14x faster                                                  |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                  |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                  |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                                   |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| telco                   | 6.73 ms                                                | 6.22 ms: 1.08x faster                                                  |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                                  |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                                   |
| pickle                  | 10.2 us                                                | 9.86 us: 1.03x faster                                                  |
| mdp                     | 2.74 sec                                               | 2.69 sec: 1.02x faster                                                 |
| generators              | 76.4 ms                                                | 75.7 ms: 1.01x faster                                                  |
| unpickle_list           | 4.92 us                                                | 4.88 us: 1.01x faster                                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| python_startup_no_site  | 5.78 ms                                                | 6.11 ms: 1.06x slower                                                  |
| regex_effbot            | 3.19 ms                                                | 3.43 ms: 1.08x slower                                                  |
| pickle_dict             | 27.6 us                                                | 30.0 us: 1.09x slower                                                  |
| dask                    | 436 ms                                                 | 494 ms: 1.13x slower                                                   |
| gc_traversal            | 3.53 ms                                                | 4.05 ms: 1.15x slower                                                  |
| coverage                | 74.7 ms                                                | 97.7 ms: 1.31x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230113-3.12.0a4+-e5bd5ad/bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad.json: mypy
