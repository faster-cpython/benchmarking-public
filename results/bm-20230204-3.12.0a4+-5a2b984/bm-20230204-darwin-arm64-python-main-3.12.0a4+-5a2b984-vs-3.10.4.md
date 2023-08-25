
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 5a2b984
- commit date: 2023-02-04
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 182 ms: 1.11x faster                                   |
| chameleon      | 5.84 ms                                                | 4.71 ms: 1.24x faster                                  |
| docutils       | 1.78 sec                                               | 1.45 sec: 1.23x faster                                 |
| html5lib       | 44.1 ms                                                | 34.8 ms: 1.27x faster                                  |
| tornado_http   | 91.9 ms                                                | 69.9 ms: 1.32x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 64.0 ms: 1.47x faster                                  |
| float          | 72.3 ms                                                | 51.9 ms: 1.39x faster                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 72.1 ms: 1.34x faster                                  |
| regex_v8       | 17.5 ms                                                | 16.2 ms: 1.08x faster                                  |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.63 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 192 us: 1.48x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.10 ms: 1.37x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 34.4 ms: 1.31x faster                                  |
| unpickle_pure_python | 203 us                                                 | 157 us: 1.30x faster                                   |
| xml_etree_parse      | 107 ms                                                 | 93.9 ms: 1.14x faster                                  |
| xml_etree_generate   | 54.3 ms                                                | 47.8 ms: 1.14x faster                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 67.8 ms: 1.07x faster                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| pickle_list          | 2.83 us                                                | 2.81 us: 1.01x faster                                  |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| unpickle             | 9.77 us                                                | 9.91 us: 1.01x slower                                  |
| unpickle_list        | 2.66 us                                                | 2.71 us: 1.02x slower                                  |
| pickle               | 7.36 us                                                | 7.57 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 9.36 ms: 1.35x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 7.35 ms: 1.32x faster                                  |
| Geometric mean         | (ref)                                                  | 1.34x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.16 ms: 1.46x faster                                  |
| genshi_xml      | 37.6 ms                                                | 28.4 ms: 1.32x faster                                  |
| django_template | 27.3 ms                                                | 20.9 ms: 1.31x faster                                  |
| genshi_text     | 18.4 ms                                                | 14.3 ms: 1.29x faster                                  |
| Geometric mean  | (ref)                                                  | 1.34x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.15 ms                                                | 2.57 ms: 2.00x faster                                  |
| logging_silent          | 119 ns                                                 | 65.7 ns: 1.81x faster                                  |
| richards                | 51.4 ms                                                | 29.7 ms: 1.73x faster                                  |
| asyncio_tcp             | 673 ms                                                 | 423 ms: 1.59x faster                                   |
| scimark_lu              | 110 ms                                                 | 70.8 ms: 1.55x faster                                  |
| async_tree_memoization  | 493 ms                                                 | 322 ms: 1.53x faster                                   |
| go                      | 165 ms                                                 | 109 ms: 1.51x faster                                   |
| raytrace                | 328 ms                                                 | 219 ms: 1.49x faster                                   |
| scimark_sor             | 127 ms                                                 | 85.3 ms: 1.48x faster                                  |
| crypto_pyaes            | 78.0 ms                                                | 52.7 ms: 1.48x faster                                  |
| pickle_pure_python      | 284 us                                                 | 192 us: 1.48x faster                                   |
| nbody                   | 94.1 ms                                                | 64.0 ms: 1.47x faster                                  |
| chaos                   | 66.8 ms                                                | 45.5 ms: 1.47x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.32 ms: 1.46x faster                                  |
| mako                    | 10.5 ms                                                | 7.16 ms: 1.46x faster                                  |
| scimark_monte_carlo     | 72.2 ms                                                | 49.8 ms: 1.45x faster                                  |
| async_tree_none         | 402 ms                                                 | 280 ms: 1.44x faster                                   |
| float                   | 72.3 ms                                                | 51.9 ms: 1.39x faster                                  |
| async_tree_io           | 1.02 sec                                               | 732 ms: 1.39x faster                                   |
| pathlib                 | 28.8 ms                                                | 20.8 ms: 1.39x faster                                  |
| json_dumps              | 8.38 ms                                                | 6.10 ms: 1.37x faster                                  |
| pycparser               | 915 ms                                                 | 669 ms: 1.37x faster                                   |
| pyflate                 | 453 ms                                                 | 333 ms: 1.36x faster                                   |
| python_startup          | 12.6 ms                                                | 9.36 ms: 1.35x faster                                  |
| regex_compile           | 96.6 ms                                                | 72.1 ms: 1.34x faster                                  |
| deepcopy_memo           | 34.5 us                                                | 25.9 us: 1.33x faster                                  |
| thrift                  | 586 us                                                 | 442 us: 1.33x faster                                   |
| spectral_norm           | 96.4 ms                                                | 72.7 ms: 1.33x faster                                  |
| python_startup_no_site  | 9.73 ms                                                | 7.35 ms: 1.32x faster                                  |
| genshi_xml              | 37.6 ms                                                | 28.4 ms: 1.32x faster                                  |
| tornado_http            | 91.9 ms                                                | 69.9 ms: 1.32x faster                                  |
| xml_etree_process       | 45.1 ms                                                | 34.4 ms: 1.31x faster                                  |
| django_template         | 27.3 ms                                                | 20.9 ms: 1.31x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 157 us: 1.30x faster                                   |
| sqlglot_parse           | 1.33 ms                                                | 1.02 ms: 1.30x faster                                  |
| pprint_pformat          | 1.24 sec                                               | 955 ms: 1.30x faster                                   |
| dulwich_log             | 37.1 ms                                                | 28.6 ms: 1.30x faster                                  |
| pprint_safe_repr        | 609 ms                                                 | 470 ms: 1.29x faster                                   |
| genshi_text             | 18.4 ms                                                | 14.3 ms: 1.29x faster                                  |
| sqlglot_transpile       | 1.54 ms                                                | 1.19 ms: 1.29x faster                                  |
| logging_format          | 5.01 us                                                | 3.93 us: 1.28x faster                                  |
| logging_simple          | 4.63 us                                                | 3.64 us: 1.27x faster                                  |
| html5lib                | 44.1 ms                                                | 34.8 ms: 1.27x faster                                  |
| deepcopy                | 278 us                                                 | 220 us: 1.26x faster                                   |
| create_gc_cycles        | 876 us                                                 | 696 us: 1.26x faster                                   |
| deepcopy_reduce         | 2.38 us                                                | 1.90 us: 1.25x faster                                  |
| async_tree_cpu_io_mixed | 670 ms                                                 | 536 ms: 1.25x faster                                   |
| fannkuch                | 317 ms                                                 | 256 ms: 1.24x faster                                   |
| chameleon               | 5.84 ms                                                | 4.71 ms: 1.24x faster                                  |
| scimark_sparse_mat_mult | 3.47 ms                                                | 2.81 ms: 1.24x faster                                  |
| docutils                | 1.78 sec                                               | 1.45 sec: 1.23x faster                                 |
| bench_thread_pool       | 548 us                                                 | 447 us: 1.23x faster                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.4 ms: 1.21x faster                                  |
| scimark_fft             | 232 ms                                                 | 192 ms: 1.21x faster                                   |
| sympy_integrate         | 13.4 ms                                                | 11.2 ms: 1.19x faster                                  |
| unpack_sequence         | 38.7 ns                                                | 32.8 ns: 1.18x faster                                  |
| async_generators        | 233 ms                                                 | 200 ms: 1.17x faster                                   |
| sympy_str               | 169 ms                                                 | 145 ms: 1.16x faster                                   |
| sympy_sum               | 94.3 ms                                                | 81.9 ms: 1.15x faster                                  |
| sqlglot_normalize       | 197 ms                                                 | 171 ms: 1.15x faster                                   |
| xml_etree_parse         | 107 ms                                                 | 93.9 ms: 1.14x faster                                  |
| sympy_expand            | 276 ms                                                 | 243 ms: 1.14x faster                                   |
| xml_etree_generate      | 54.3 ms                                                | 47.8 ms: 1.14x faster                                  |
| nqueens                 | 68.1 ms                                                | 60.8 ms: 1.12x faster                                  |
| 2to3                    | 202 ms                                                 | 182 ms: 1.11x faster                                   |
| mdp                     | 1.67 sec                                               | 1.52 sec: 1.10x faster                                 |
| json                    | 3.10 ms                                                | 2.83 ms: 1.09x faster                                  |
| regex_v8                | 17.5 ms                                                | 16.2 ms: 1.08x faster                                  |
| coroutines              | 20.2 ms                                                | 18.8 ms: 1.08x faster                                  |
| telco                   | 3.68 ms                                                | 3.43 ms: 1.07x faster                                  |
| xml_etree_iterparse     | 72.6 ms                                                | 67.8 ms: 1.07x faster                                  |
| regex_dna               | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| sqlite_synth            | 1.47 us                                                | 1.40 us: 1.06x faster                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                  |
| meteor_contest          | 78.6 ms                                                | 75.9 ms: 1.04x faster                                  |
| pickle_list             | 2.83 us                                                | 2.81 us: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 283 ms: 1.00x slower                                   |
| gc_traversal            | 2.40 ms                                                | 2.41 ms: 1.01x slower                                  |
| pickle_dict             | 17.8 us                                                | 18.0 us: 1.01x slower                                  |
| unpickle                | 9.77 us                                                | 9.91 us: 1.01x slower                                  |
| unpickle_list           | 2.66 us                                                | 2.71 us: 1.02x slower                                  |
| pickle                  | 7.36 us                                                | 7.57 us: 1.03x slower                                  |
| generators              | 32.9 ms                                                | 34.1 ms: 1.04x slower                                  |
| bench_mp_pool           | 41.0 ms                                                | 42.9 ms: 1.05x slower                                  |
| regex_effbot            | 2.45 ms                                                | 2.63 ms: 1.07x slower                                  |
| dask                    | 258 ms                                                 | 319 ms: 1.24x slower                                   |
| coverage                | 40.8 ms                                                | 57.1 ms: 1.40x slower                                  |
| Geometric mean          | (ref)                                                  | 1.24x faster                                           |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230204-3.12.0a4+-5a2b984/bm-20230204-darwin-arm64-python-main-3.12.0a4+-5a2b984.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x
