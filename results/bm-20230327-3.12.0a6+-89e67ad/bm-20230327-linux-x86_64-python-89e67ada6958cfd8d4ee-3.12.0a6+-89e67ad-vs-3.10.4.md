
# Results vs. 3.10.4

- fork: python
- ref: 89e67ada6958cfd8d4ee
- machine: linux-x86_64
- commit hash: 89e67ad
- commit date: 2023-03-27
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.46 ms: 1.40x faster                                                  |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.38x faster                                                  |
| tornado_http   | 127 ms                                                 | 91.2 ms: 1.40x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.3 ms: 1.62x faster                                                  |
| float          | 111 ms                                                 | 73.4 ms: 1.51x faster                                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                  |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.52 ms: 1.42x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 56.0 ms: 1.34x faster                                                  |
| json_loads           | 28.8 us                                                | 24.1 us: 1.20x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.9 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.15 us: 1.10x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                                  |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                  |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.2 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.80 ms: 1.61x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.95 ms: 1.48x faster                                                  |
| genshi_text     | 30.3 ms                                                | 21.8 ms: 1.39x faster                                                  |
| django_template | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 47.4 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 28.9 ms: 2.66x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                  |
| logging_silent          | 175 ns                                                 | 94.5 ns: 1.85x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 502 ms: 1.84x faster                                                   |
| scimark_sor             | 197 ms                                                 | 111 ms: 1.77x faster                                                   |
| richards                | 74.9 ms                                                | 43.5 ms: 1.72x faster                                                  |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                                   |
| go                      | 229 ms                                                 | 139 ms: 1.65x faster                                                   |
| spectral_norm           | 150 ms                                                 | 91.8 ms: 1.63x faster                                                  |
| nbody                   | 142 ms                                                 | 87.3 ms: 1.62x faster                                                  |
| pyflate                 | 673 ms                                                 | 418 ms: 1.61x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 73.6 ms: 1.61x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.80 ms: 1.61x faster                                                  |
| chaos                   | 106 ms                                                 | 66.7 ms: 1.59x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.02 ms: 1.58x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 69.1 ms: 1.57x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 33.6 us: 1.56x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 41.8 ns: 1.55x faster                                                  |
| float                   | 111 ms                                                 | 73.4 ms: 1.51x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                                   |
| mako                    | 14.8 ms                                                | 9.95 ms: 1.48x faster                                                  |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.48x faster                                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.52 ms: 1.42x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.42x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.46 ms: 1.40x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.77 us: 1.40x faster                                                  |
| logging_format          | 8.91 us                                                | 6.37 us: 1.40x faster                                                  |
| tornado_http            | 127 ms                                                 | 91.2 ms: 1.40x faster                                                  |
| genshi_text             | 30.3 ms                                                | 21.8 ms: 1.39x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                                 |
| django_template         | 45.9 ms                                                | 33.1 ms: 1.39x faster                                                  |
| coroutines              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                                  |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.38x faster                                                  |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 696 ms: 1.37x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                                 |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                   |
| scimark_fft             | 424 ms                                                 | 313 ms: 1.35x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                                 |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                                   |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 56.0 ms: 1.34x faster                                                  |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 47.4 ms: 1.33x faster                                                  |
| thrift                  | 1.03 ms                                                | 781 us: 1.32x faster                                                   |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.92 us: 1.31x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                                   |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 738 ms: 1.29x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.25 ms: 1.28x faster                                                  |
| fannkuch                | 486 ms                                                 | 383 ms: 1.27x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 107 ms: 1.27x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.5 ms: 1.27x faster                                                  |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.26x faster                                                 |
| nqueens                 | 100 ms                                                 | 80.4 ms: 1.24x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.5 ms: 1.21x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 788 us: 1.20x faster                                                   |
| json_loads              | 28.8 us                                                | 24.1 us: 1.20x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                  |
| sympy_expand            | 545 ms                                                 | 460 ms: 1.18x faster                                                   |
| json                    | 5.42 ms                                                | 4.64 ms: 1.17x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.9 ms: 1.16x faster                                                  |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                  |
| comprehensions          | 26.8 us                                                | 23.8 us: 1.13x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.13x faster                                                 |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.12x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                                   |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                  |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.15 us: 1.10x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                                   |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                                  |
| gc_traversal            | 3.84 ms                                                | 3.67 ms: 1.05x faster                                                  |
| async_generators        | 425 ms                                                 | 410 ms: 1.04x faster                                                   |
| telco                   | 6.54 ms                                                | 6.46 ms: 1.01x faster                                                  |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                  |
| unpickle_list           | 4.82 us                                                | 5.08 us: 1.05x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.43 ms: 1.06x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.2 us: 1.14x slower                                                  |
| dask                    | 423 ms                                                 | 510 ms: 1.21x slower                                                   |
| coverage                | 72.8 ms                                                | 96.7 ms: 1.33x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
