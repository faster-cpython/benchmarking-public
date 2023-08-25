
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 06249ec
- commit date: 2023-04-01
- overall geometric mean: 1.20x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 168 ms: 1.20x faster                                   |
| chameleon      | 5.84 ms                                                | 4.50 ms: 1.30x faster                                  |
| docutils       | 1.78 sec                                               | 1.49 sec: 1.19x faster                                 |
| html5lib       | 44.1 ms                                                | 36.8 ms: 1.20x faster                                  |
| tornado_http   | 91.9 ms                                                | 69.7 ms: 1.32x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 60.4 ms: 1.56x faster                                  |
| float          | 72.3 ms                                                | 53.1 ms: 1.36x faster                                  |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 76.8 ms: 1.26x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 160 ms                                                 | 152 ms: 1.05x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.70 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 193 us: 1.47x faster                                   |
| unpickle_pure_python | 203 us                                                 | 148 us: 1.37x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.23 ms: 1.35x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 36.8 ms: 1.22x faster                                  |
| xml_etree_parse      | 107 ms                                                 | 99.1 ms: 1.08x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 51.3 ms: 1.06x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 71.3 ms: 1.02x faster                                  |
| unpickle             | 9.77 us                                                | 9.67 us: 1.01x faster                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| unpickle_list        | 2.66 us                                                | 2.69 us: 1.01x slower                                  |
| pickle               | 7.36 us                                                | 7.47 us: 1.02x slower                                  |
| pickle_list          | 2.83 us                                                | 2.91 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.4 ms: 1.02x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 10.2 ms: 1.05x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.40 ms: 1.42x faster                                  |
| genshi_xml      | 37.6 ms                                                | 29.4 ms: 1.28x faster                                  |
| django_template | 27.3 ms                                                | 21.8 ms: 1.25x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.8 ms: 1.25x faster                                  |
| Geometric mean  | (ref)                                                  | 1.30x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-darwin-arm64-python-main-3.12.0a6+-06249ec |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.61 ms: 1.97x faster                                  |
| logging_silent          | 119 ns                                                 | 66.8 ns: 1.78x faster                                  |
| richards                | 51.4 ms                                                | 31.4 ms: 1.64x faster                                  |
| nbody                   | 94.1 ms                                                | 60.4 ms: 1.56x faster                                  |
| scimark_lu              | 110 ms                                                 | 71.4 ms: 1.54x faster                                  |
| asyncio_tcp             | 673 ms                                                 | 439 ms: 1.53x faster                                   |
| async_tree_memoization  | 493 ms                                                 | 330 ms: 1.49x faster                                   |
| raytrace                | 328 ms                                                 | 222 ms: 1.47x faster                                   |
| pickle_pure_python      | 284 us                                                 | 193 us: 1.47x faster                                   |
| scimark_sor             | 127 ms                                                 | 88.3 ms: 1.43x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.43 ms: 1.43x faster                                  |
| go                      | 165 ms                                                 | 116 ms: 1.42x faster                                   |
| crypto_pyaes            | 78.0 ms                                                | 54.9 ms: 1.42x faster                                  |
| mako                    | 10.5 ms                                                | 7.40 ms: 1.42x faster                                  |
| chaos                   | 66.8 ms                                                | 47.5 ms: 1.41x faster                                  |
| async_tree_none         | 402 ms                                                 | 289 ms: 1.39x faster                                   |
| async_tree_io           | 1.02 sec                                               | 739 ms: 1.38x faster                                   |
| unpickle_pure_python    | 203 us                                                 | 148 us: 1.37x faster                                   |
| scimark_monte_carlo     | 72.2 ms                                                | 53.0 ms: 1.36x faster                                  |
| float                   | 72.3 ms                                                | 53.1 ms: 1.36x faster                                  |
| json_dumps              | 8.38 ms                                                | 6.23 ms: 1.35x faster                                  |
| pycparser               | 915 ms                                                 | 680 ms: 1.34x faster                                   |
| deepcopy_memo           | 34.5 us                                                | 26.0 us: 1.33x faster                                  |
| pyflate                 | 453 ms                                                 | 343 ms: 1.32x faster                                   |
| tornado_http            | 91.9 ms                                                | 69.7 ms: 1.32x faster                                  |
| spectral_norm           | 96.4 ms                                                | 73.1 ms: 1.32x faster                                  |
| chameleon               | 5.84 ms                                                | 4.50 ms: 1.30x faster                                  |
| genshi_xml              | 37.6 ms                                                | 29.4 ms: 1.28x faster                                  |
| pprint_safe_repr        | 609 ms                                                 | 477 ms: 1.28x faster                                   |
| pprint_pformat          | 1.24 sec                                               | 973 ms: 1.27x faster                                   |
| thrift                  | 586 us                                                 | 464 us: 1.26x faster                                   |
| logging_format          | 5.01 us                                                | 3.97 us: 1.26x faster                                  |
| regex_compile           | 96.6 ms                                                | 76.8 ms: 1.26x faster                                  |
| logging_simple          | 4.63 us                                                | 3.68 us: 1.26x faster                                  |
| django_template         | 27.3 ms                                                | 21.8 ms: 1.25x faster                                  |
| deepcopy                | 278 us                                                 | 222 us: 1.25x faster                                   |
| create_gc_cycles        | 876 us                                                 | 701 us: 1.25x faster                                   |
| genshi_text             | 18.4 ms                                                | 14.8 ms: 1.25x faster                                  |
| sqlglot_parse           | 1.33 ms                                                | 1.07 ms: 1.24x faster                                  |
| dulwich_log             | 37.1 ms                                                | 30.0 ms: 1.24x faster                                  |
| sqlglot_transpile       | 1.54 ms                                                | 1.25 ms: 1.23x faster                                  |
| scimark_fft             | 232 ms                                                 | 188 ms: 1.23x faster                                   |
| async_tree_cpu_io_mixed | 670 ms                                                 | 545 ms: 1.23x faster                                   |
| sqlalchemy_imperative   | 9.03 ms                                                | 7.34 ms: 1.23x faster                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.83 ms: 1.23x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 36.8 ms: 1.22x faster                                  |
| deepcopy_reduce         | 2.38 us                                                | 1.95 us: 1.22x faster                                  |
| 2to3                    | 202 ms                                                 | 168 ms: 1.20x faster                                   |
| html5lib                | 44.1 ms                                                | 36.8 ms: 1.20x faster                                  |
| generators              | 32.9 ms                                                | 27.6 ms: 1.19x faster                                  |
| docutils                | 1.78 sec                                               | 1.49 sec: 1.19x faster                                 |
| unpack_sequence         | 38.7 ns                                                | 32.9 ns: 1.18x faster                                  |
| sqlglot_optimize        | 38.0 ms                                                | 32.3 ms: 1.18x faster                                  |
| fannkuch                | 317 ms                                                 | 271 ms: 1.17x faster                                   |
| mypy2                   | 308 ms                                                 | 264 ms: 1.17x faster                                   |
| bench_thread_pool       | 548 us                                                 | 472 us: 1.16x faster                                   |
| sqlalchemy_declarative  | 74.8 ms                                                | 64.4 ms: 1.16x faster                                  |
| sympy_integrate         | 13.4 ms                                                | 11.8 ms: 1.13x faster                                  |
| sqlglot_normalize       | 197 ms                                                 | 176 ms: 1.12x faster                                   |
| json                    | 3.10 ms                                                | 2.80 ms: 1.11x faster                                  |
| sympy_expand            | 276 ms                                                 | 250 ms: 1.10x faster                                   |
| regex_v8                | 17.5 ms                                                | 16.1 ms: 1.09x faster                                  |
| mdp                     | 1.67 sec                                               | 1.54 sec: 1.09x faster                                 |
| sympy_str               | 169 ms                                                 | 156 ms: 1.09x faster                                   |
| xml_etree_parse         | 107 ms                                                 | 99.1 ms: 1.08x faster                                  |
| meteor_contest          | 78.6 ms                                                | 72.7 ms: 1.08x faster                                  |
| sqlite_synth            | 1.47 us                                                | 1.36 us: 1.08x faster                                  |
| nqueens                 | 68.1 ms                                                | 63.3 ms: 1.08x faster                                  |
| coroutines              | 20.2 ms                                                | 18.9 ms: 1.07x faster                                  |
| sympy_sum               | 94.3 ms                                                | 88.8 ms: 1.06x faster                                  |
| xml_etree_generate      | 54.3 ms                                                | 51.3 ms: 1.06x faster                                  |
| regex_dna               | 160 ms                                                 | 152 ms: 1.05x faster                                   |
| pathlib                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                  |
| telco                   | 3.68 ms                                                | 3.54 ms: 1.04x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.03x faster                                  |
| python_startup          | 12.6 ms                                                | 12.4 ms: 1.02x faster                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 71.3 ms: 1.02x faster                                  |
| unpickle                | 9.77 us                                                | 9.67 us: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 280 ms: 1.01x faster                                   |
| comprehensions          | 17.7 us                                                | 17.8 us: 1.01x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| unpickle_list           | 2.66 us                                                | 2.69 us: 1.01x slower                                  |
| gc_traversal            | 2.40 ms                                                | 2.43 ms: 1.01x slower                                  |
| pickle                  | 7.36 us                                                | 7.47 us: 1.02x slower                                  |
| pickle_list             | 2.83 us                                                | 2.91 us: 1.03x slower                                  |
| python_startup_no_site  | 9.73 ms                                                | 10.2 ms: 1.05x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.70 ms: 1.10x slower                                  |
| bench_mp_pool           | 41.0 ms                                                | 46.4 ms: 1.13x slower                                  |
| async_generators        | 233 ms                                                 | 265 ms: 1.14x slower                                   |
| dask                    | 258 ms                                                 | 327 ms: 1.27x slower                                   |
| coverage                | 40.8 ms                                                | 60.5 ms: 1.48x slower                                  |
| Geometric mean          | (ref)                                                  | 1.20x faster                                           |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
