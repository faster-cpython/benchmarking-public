
# Results vs. 3.10.4

- fork: python
- ref: e5bd5ad70d9e549eeb80
- machine: linux-x86_64
- commit hash: e5bd5ad
- commit date: 2023-01-13
- overall geometric mean: 1.31x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.32x faster                                                   |
| chameleon      | 8.86 ms                                                | 6.25 ms: 1.42x faster                                                  |
| docutils       | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                 |
| html5lib       | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                  |
| tornado_http   | 128 ms                                                 | 93.2 ms: 1.38x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.7 ms: 1.50x faster                                                  |
| nbody          | 136 ms                                                 | 97.0 ms: 1.40x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                   |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                                   |
| regex_effbot   | 3.21 ms                                                | 3.43 ms: 1.07x slower                                                  |
| regex_v8       | 25.0 ms                                                | 21.6 ms: 1.15x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.35 ms: 1.44x faster                                                  |
| json_loads           | 28.9 us                                                | 24.4 us: 1.18x faster                                                  |
| pickle               | 10.1 us                                                | 9.86 us: 1.03x faster                                                  |
| pickle_dict          | 28.3 us                                                | 30.0 us: 1.06x slower                                                  |
| pickle_list          | 4.50 us                                                | 3.99 us: 1.13x faster                                                  |
| pickle_pure_python   | 453 us                                                 | 281 us: 1.61x faster                                                   |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                                  |
| unpickle_list        | 4.99 us                                                | 4.88 us: 1.02x faster                                                  |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 110 ms                                                 | 107 ms: 1.03x faster                                                   |
| xml_etree_generate   | 93.3 ms                                                | 76.3 ms: 1.22x faster                                                  |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.40x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.54 ms: 1.63x faster                                                  |
| python_startup_no_site | 5.76 ms                                                | 6.11 ms: 1.06x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 31.9 ms: 1.45x faster                                                  |
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                  |
| genshi_xml      | 63.6 ms                                                | 46.6 ms: 1.36x faster                                                  |
| mako            | 14.3 ms                                                | 9.71 ms: 1.47x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 251 ms: 1.32x faster                                                   |
| aiohttp                 | 1.34 ms                                                | 997 us: 1.34x faster                                                   |
| async_generators        | 428 ms                                                 | 351 ms: 1.22x faster                                                   |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 737 ms: 1.29x faster                                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                 |
| async_tree_memoization  | 854 ms                                                 | 617 ms: 1.38x faster                                                   |
| chameleon               | 8.86 ms                                                | 6.25 ms: 1.42x faster                                                  |
| chaos                   | 104 ms                                                 | 68.0 ms: 1.53x faster                                                  |
| bench_thread_pool       | 943 us                                                 | 778 us: 1.21x faster                                                   |
| coroutines              | 31.7 ms                                                | 24.6 ms: 1.28x faster                                                  |
| coverage                | 75.3 ms                                                | 97.7 ms: 1.30x slower                                                  |
| crypto_pyaes            | 118 ms                                                 | 74.8 ms: 1.57x faster                                                  |
| deepcopy                | 429 us                                                 | 329 us: 1.31x faster                                                   |
| deepcopy_reduce         | 3.75 us                                                | 2.91 us: 1.29x faster                                                  |
| deepcopy_memo           | 50.0 us                                                | 33.7 us: 1.48x faster                                                  |
| deltablue               | 7.39 ms                                                | 3.17 ms: 2.33x faster                                                  |
| django_template         | 46.3 ms                                                | 31.9 ms: 1.45x faster                                                  |
| docutils                | 3.18 sec                                               | 2.48 sec: 1.28x faster                                                 |
| dulwich_log             | 75.5 ms                                                | 62.2 ms: 1.21x faster                                                  |
| fannkuch                | 477 ms                                                 | 366 ms: 1.30x faster                                                   |
| float                   | 108 ms                                                 | 71.7 ms: 1.50x faster                                                  |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                                  |
| genshi_xml              | 63.6 ms                                                | 46.6 ms: 1.36x faster                                                  |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                   |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                                  |
| hexiom                  | 9.42 ms                                                | 6.03 ms: 1.56x faster                                                  |
| html5lib                | 85.8 ms                                                | 59.7 ms: 1.44x faster                                                  |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.35 ms: 1.44x faster                                                  |
| json_loads              | 28.9 us                                                | 24.4 us: 1.18x faster                                                  |
| logging_format          | 8.92 us                                                | 6.22 us: 1.44x faster                                                  |
| logging_silent          | 173 ns                                                 | 89.4 ns: 1.94x faster                                                  |
| logging_simple          | 8.06 us                                                | 5.66 us: 1.42x faster                                                  |
| mako                    | 14.3 ms                                                | 9.71 ms: 1.47x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.69 sec: 1.05x faster                                                 |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                   |
| mypy                    | 1.01 sec                                               | 809 ms: 1.25x faster                                                   |
| nbody                   | 136 ms                                                 | 97.0 ms: 1.40x faster                                                  |
| nqueens                 | 99.3 ms                                                | 77.8 ms: 1.28x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                  |
| pickle                  | 10.1 us                                                | 9.86 us: 1.03x faster                                                  |
| pickle_dict             | 28.3 us                                                | 30.0 us: 1.06x slower                                                  |
| pickle_list             | 4.50 us                                                | 3.99 us: 1.13x faster                                                  |
| pickle_pure_python      | 453 us                                                 | 281 us: 1.61x faster                                                   |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| pprint_safe_repr        | 943 ms                                                 | 663 ms: 1.42x faster                                                   |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                 |
| pycparser               | 1.51 sec                                               | 1.09 sec: 1.38x faster                                                 |
| pyflate                 | 675 ms                                                 | 401 ms: 1.69x faster                                                   |
| python_startup          | 13.9 ms                                                | 8.54 ms: 1.63x faster                                                  |
| python_startup_no_site  | 5.76 ms                                                | 6.11 ms: 1.06x slower                                                  |
| raytrace                | 461 ms                                                 | 279 ms: 1.65x faster                                                   |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                   |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                                   |
| regex_effbot            | 3.21 ms                                                | 3.43 ms: 1.07x slower                                                  |
| regex_v8                | 25.0 ms                                                | 21.6 ms: 1.15x faster                                                  |
| richards                | 71.4 ms                                                | 41.2 ms: 1.73x faster                                                  |
| scimark_fft             | 414 ms                                                 | 312 ms: 1.33x faster                                                   |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                                   |
| scimark_monte_carlo     | 105 ms                                                 | 64.3 ms: 1.63x faster                                                  |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.82x faster                                                   |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.15 ms: 1.32x faster                                                  |
| spectral_norm           | 148 ms                                                 | 94.5 ms: 1.57x faster                                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.68 ms: 1.44x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                   |
| sqlite_synth            | 2.90 us                                                | 2.61 us: 1.11x faster                                                  |
| sympy_expand            | 537 ms                                                 | 454 ms: 1.18x faster                                                   |
| sympy_integrate         | 23.9 ms                                                | 20.3 ms: 1.18x faster                                                  |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.12x faster                                                   |
| sympy_str               | 324 ms                                                 | 282 ms: 1.15x faster                                                   |
| telco                   | 6.68 ms                                                | 6.22 ms: 1.07x faster                                                  |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                                   |
| tornado_http            | 128 ms                                                 | 93.2 ms: 1.38x faster                                                  |
| unpack_sequence         | 59.5 ns                                                | 44.5 ns: 1.34x faster                                                  |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                                  |
| unpickle_list           | 4.99 us                                                | 4.88 us: 1.02x faster                                                  |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| xml_etree_iterparse     | 110 ms                                                 | 107 ms: 1.03x faster                                                   |
| xml_etree_generate      | 93.3 ms                                                | 76.3 ms: 1.22x faster                                                  |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.40x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, generators
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230113-3.12.0a4+-e5bd5ad/bm-20230113-linux-x86_64-python-e5bd5ad70d9e549eeb80-3.12.0a4+-e5bd5ad.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
